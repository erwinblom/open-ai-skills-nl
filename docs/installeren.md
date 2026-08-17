# Skills installeren en gebruiken

De kern van iedere skill is een gewone map met een `SKILL.md`. De bestanden in `agents/openai.yaml` voegen metadata toe voor OpenAI-producten, maar zijn niet nodig voor agents die alleen het open Agent Skills-formaat lezen.

## Kies eerst wat je nodig hebt

Je hoeft niet de hele repository te installeren.

- Voor redactie: installeer één of beide skills uit `skills/tekstploeg/`.
- Voor een compleet innovatieproces: installeer de vijf skills uit `skills/innovatieploeg/`.
- Voor één innovatiestap: installeer alleen de passende skill.

## Controle vóór installatie

Een skill bevat instructies die je AI-agent zal volgen. Controleer daarom minimaal:

1. de frontmatter bovenaan `SKILL.md`;
2. de volledige werkwijze in `SKILL.md`;
3. bestanden in `references/`, `scripts/` en `assets/`;
4. eventuele gereedschappen of externe diensten die de skill vraagt te gebruiken.

Deze repository bevat geen uitvoerbare scripts binnen de individuele skills en vereist geen betaalde dienst.

## Zonder terminal: downloaden en als instructie gebruiken

1. [Download de repository als ZIP](https://github.com/erwinblom/open-ai-skills-nl/archive/refs/heads/main.zip).
2. Pak de ZIP uit.
3. Kies één map onder `skills/tekstploeg/` of `skills/innovatieploeg/`.
4. Kan je AI-tool skills importeren, maak dan van die ene map een ZIP en upload hem.
5. Kan je tool geen skills importeren, open `SKILL.md` en voeg de inhoud toe als projectinstructie of eerste bericht. Voeg een referentiebestand pas toe wanneer `SKILL.md` zegt dat het nodig is.

Een mogelijke opdracht:

```text
Controleer deze skillmap en installeer hem als hij veilig en geldig is.
Vertel daarna in één alinea wanneer ik hem kan gebruiken.
```

## ChatGPT en Codex

In ChatGPT selecteer je een geïnstalleerde skill met `@`. In Codex noem je hem met `$` of gebruik je `/skills`. ChatGPT en Codex kunnen een skill ook automatisch kiezen op basis van de beschrijving.

Voor lokaal gebruik met Codex kopieer je de skill naar `$HOME/.agents/skills`:

Kloon eerst de repository:

```bash
git clone https://github.com/erwinblom/open-ai-skills-nl.git
cd open-ai-skills-nl
```

Kopieer daarna de gewenste map:

```bash
mkdir -p ~/.agents/skills
cp -R skills/tekstploeg/de-tegenlezer ~/.agents/skills/
```

Voor alle zeven skills:

```bash
mkdir -p ~/.agents/skills
cp -R skills/tekstploeg/* ~/.agents/skills/
cp -R skills/innovatieploeg/* ~/.agents/skills/
```

Voor één repository gebruik je `.agents/skills/` in die repository. Codex detecteert wijzigingen normaal automatisch. Zie de [officiële documentatie voor ChatGPT en Codex](https://learn.chatgpt.com/docs/build-skills).

## Andere AI-tools

### Claude Code

Claude Code gebruikt eveneens skillmappen met een `SKILL.md`. Voor persoonlijk gebruik kopieer je een skill naar `~/.claude/skills/`. Voor één project gebruik je `.claude/skills/`:

```bash
mkdir -p ~/.claude/skills
cp -R skills/tekstploeg/de-tegenlezer ~/.claude/skills/
```

Roep de skill aan met een slash:

```text
/de-tegenlezer
```

Claude kan hem op basis van de beschrijving ook automatisch kiezen. Zie de [officiële Claude Code-documentatie over skills](https://code.claude.com/docs/en/skills).

### Gemini CLI

Gemini CLI volgt het open Agent Skills-formaat. De eenvoudigste installatie van één lokale skill is:

```bash
gemini skills install ./skills/innovatieploeg/de-kansverkenner
```

Je kunt een skill ook kopiëren naar `~/.gemini/skills/` voor persoonlijk gebruik of `.gemini/skills/` voor een project. Gemini ondersteunt daarnaast de interoperabele map `.agents/skills/`.

Controleer de installatie met:

```bash
gemini skills list
```

Zie de [officiële Gemini CLI-documentatie over Agent Skills](https://geminicli.com/docs/cli/skills/).

### GitHub Copilot in VS Code

VS Code en GitHub Copilot ontdekken projectskills in:

- `.github/skills/`
- `.claude/skills/`
- `.agents/skills/`

Voor persoonlijk gebruik worden onder meer `~/.copilot/skills/`, `~/.claude/skills/` en `~/.agents/skills/` ondersteund. Kopieer bijvoorbeeld:

```bash
mkdir -p .github/skills
cp -R skills/tekstploeg/de-cliche-verwijderaar .github/skills/
```

Open daarna Copilot Chat. Met `/skills` kun je de Skills-configuratie openen. Zie de [officiële VS Code-documentatie over Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).

### Eén gedeelde map voor meerdere agents

Gemini CLI en GitHub Copilot ondersteunen `.agents/skills/` als interoperabele locatie. Claude Code gebruikt standaard `.claude/skills/`. Wanneer meerdere tools hetzelfde project gebruiken, kun je de skills in `.agents/skills/` bewaren en voor een tool die deze map niet ontdekt een kopie of symlink in de eigen skillsmap maken.

Controleer per tool welke map voorrang krijgt als dezelfde skill op meerdere plaatsen staat.

### Chattools zonder skillondersteuning

De werkwijze blijft bruikbaar in Cursor en andere chatomgevingen die geen lokale skillmap laden:

1. Open de gewenste `SKILL.md`.
2. Voeg de inhoud toe als projectinstructie, systeemprompt of eerste bericht.
3. Voeg alleen de referentiebestanden toe waarnaar de skill voor jouw opdracht verwijst.
4. Geef daarna materiaal en opdracht.

Voorbeeld:

```text
Volg de bijgevoegde instructies uit De Tegenlezer.
Lees dit voorstel kritisch, maar herschrijf het nog niet.
```

Automatische activering en progressieve inlading ontbreken dan meestal. De inhoudelijke methode blijft gelijk.

## Een skill aanroepen

Gebruik de aanroepvorm van je tool: `@` in ChatGPT, `$` in Codex, `/` in Claude Code of de gewone naam wanneer je `SKILL.md` als instructie hebt toegevoegd. In Codex wordt dat bijvoorbeeld:

```text
Gebruik $de-klantverkenner. Doe een snelle synthetische stresstest van dit productidee en ontwerp daarna vragen voor echte klanten.
```

Je kunt ook gewoon een passende opdracht geven. Een agent kan de skill dan op basis van de beschrijving automatisch kiezen.

## Context meegeven

Een skill werkt beter wanneer je naast het materiaal ook vermeldt:

- wat je wilt beslissen of opleveren;
- voor wie het bedoeld is;
- wat vaststaat;
- wat nog onzeker is;
- welke grenzen gelden voor tijd, geld, toon, privacy of techniek.

Geef geen persoonsgegevens, bedrijfsgeheimen of vertrouwelijke documenten aan een omgeving die daarvoor niet is goedgekeurd.

## Bijwerken

Bij een lokale installatie vervang je de oude skillmap door de nieuwe versie uit de repository. Lees wijzigingen eerst door wanneer je de skill in gevoelige of vaste werkprocessen gebruikt.

## Verwijderen

Verwijder de geïnstalleerde skillmap uit de skillsmap van je omgeving. Bestaande gesprekken of documenten worden hierdoor niet verwijderd.
