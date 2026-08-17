#!/usr/bin/env python3
"""Controleer de structuur, metadata en lokale links van alle skills."""

from pathlib import Path
import re
import sys
import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
LINK_RE = re.compile(r"\[[^]]+\]\((references/[^)]+)\)")
MARKDOWN_LINK_RE = re.compile(r"\[[^]]+\]\(([^)]+)\)")


class UniqueKeyLoader(yaml.SafeLoader):
    """YAML-loader die dubbele sleutels weigert."""


def construct_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    mapping: dict = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.YAMLError(f"dubbele sleutel: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_mapping,
)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def validate_openai_yaml(skill_dir: Path, errors: list[str]) -> None:
    yaml_file = skill_dir / "agents" / "openai.yaml"
    if not yaml_file.is_file():
        errors.append(f"{skill_dir}: agents/openai.yaml ontbreekt")
        return

    try:
        data = yaml.load(yaml_file.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        errors.append(f"{yaml_file}: ongeldige YAML: {exc}")
        return

    if not isinstance(data, dict):
        errors.append(f"{yaml_file}: de hoofdstructuur moet een mapping zijn")
        return

    expected_root = {"interface", "policy"}
    if set(data) != expected_root:
        errors.append(f"{yaml_file}: verwachte hoofdsleutels {sorted(expected_root)}, gevonden {sorted(data)}")

    interface = data.get("interface")
    policy = data.get("policy")
    expected_interface = {"display_name", "short_description", "default_prompt", "icon_small", "icon_large"}
    if not isinstance(interface, dict):
        errors.append(f"{yaml_file}: interface moet een mapping zijn")
        return
    if set(interface) != expected_interface:
        errors.append(f"{yaml_file}: onjuiste interfacevelden: {sorted(interface)}")

    for key in ("display_name", "short_description", "default_prompt"):
        if not isinstance(interface.get(key), str) or not interface[key].strip():
            errors.append(f"{yaml_file}: {key} moet een niet-lege tekst zijn")

    skill_name = skill_dir.name
    prompt = interface.get("default_prompt", "")
    if isinstance(prompt, str) and f"${skill_name}" not in prompt:
        errors.append(f"{yaml_file}: default_prompt moet ${skill_name} noemen")

    if policy != {"allow_implicit_invocation": True}:
        errors.append(f"{yaml_file}: policy moet alleen allow_implicit_invocation: true bevatten")

    for key in ("icon_small", "icon_large"):
        icon_path = interface.get(key)
        if not isinstance(icon_path, str):
            errors.append(f"{yaml_file}: {key} moet tekst zijn")
            continue
        if not icon_path.startswith("./assets/"):
            errors.append(f"{yaml_file}: {key} moet naar ./assets/ wijzen")
        if not (skill_dir / icon_path).is_file():
            errors.append(f"{yaml_file}: icoon ontbreekt: {icon_path}")


def main() -> int:
    errors: list[str] = []
    skill_files = sorted(SKILLS_ROOT.glob("*/*/SKILL.md"))
    if not skill_files:
        errors.append("Geen skills gevonden.")

    names: set[str] = set()
    for skill_file in skill_files:
        skill_dir = skill_file.parent
        text = skill_file.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        name = meta.get("name", "")
        description = meta.get("description", "")

        if not NAME_RE.fullmatch(name):
            errors.append(f"{skill_file}: ongeldige of ontbrekende naam")
        if name != skill_dir.name:
            errors.append(f"{skill_file}: naam en map komen niet overeen")
        if name in names:
            errors.append(f"{skill_file}: dubbele skillnaam {name}")
        names.add(name)
        if len(description) < 40:
            errors.append(f"{skill_file}: beschrijving is te kort")
        validate_openai_yaml(skill_dir, errors)

        for relative in LINK_RE.findall(text):
            if not (skill_dir / relative).is_file():
                errors.append(f"{skill_file}: ontbrekende referentie {relative}")

    for markdown_file in sorted(ROOT.rglob("*.md")):
        text = markdown_file.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0]
            if path_part and not (markdown_file.parent / path_part).exists():
                errors.append(f"{markdown_file}: ontbrekende link {target}")

    if errors:
        print("Validatie mislukt:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Alle {len(skill_files)} skills zijn geldig.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
