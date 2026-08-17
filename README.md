# Open-source AI Skills NL

Open-source Agent Skills in het Nederlands. Praktisch, kritisch en bedoeld om echt werk mee te doen. De kern volgt het open `SKILL.md`-formaat en is daardoor bruikbaar in meerdere AI-tools.

Dit is een onafhankelijk project van Erwin Blom en is niet gemaakt of uitgegeven door OpenAI, Anthropic, Google, GitHub of Microsoft.

> **De methode is gratis. De begeleiding maakt het verschil.**

Deze repository bevat twee samenhangende collecties:

- **De Tekstploeg** helpt teksten scherper, helderder en geloofwaardiger maken.
- **De Innovatieploeg** helpt organisaties van kans naar bewijs gaan.

Iedere skill is zelfstandig te gebruiken. Samen vormen de skills een werkproces.

## De Tekstploeg

| Skill | Doel |
|---|---|
| [De Cliché-verwijderaar](skills/tekstploeg/de-cliche-verwijderaar/SKILL.md) | Verwijdert clichés, lege taal en voorspelbare AI-cadans zonder de stem van de schrijver kwijt te raken. |
| [De Tegenlezer](skills/tekstploeg/de-tegenlezer/SKILL.md) | Test redenering, bewijs, structuur, blinde vlekken en weerstand bij de lezer. |

[Lees hoe De Tekstploeg werkt](skills/tekstploeg/README.md) of bekijk [het tekstvoorbeeld](examples/tekstploeg.md).

## De Innovatieploeg

| Stap | Skill | Resultaat |
|---|---|---|
| 1 | [De Kansverkenner](skills/innovatieploeg/de-kansverkenner/SKILL.md) | Drie concrete businesskansen en een eerste keuze. |
| 2 | [De Aannamejager](skills/innovatieploeg/de-aannamejager/SKILL.md) | De riskantste aannames en een testvolgorde. |
| 3 | [De Klantverkenner](skills/innovatieploeg/de-klantverkenner/SKILL.md) | Een synthetische perspectiefstresstest en echte onderzoeksvragen. |
| 4 | [De Eerste-versiebouwer](skills/innovatieploeg/de-eerste-versiebouwer/SKILL.md) | De kleinste bruikbare versie; een artefact als de gebruikte agent kan bouwen. |
| 5 | [De Bewijsweger](skills/innovatieploeg/de-bewijsweger/SKILL.md) | Een besluit op basis van echte resultaten: doorgaan, aanpassen, opnieuw testen of stoppen. |

[Lees de volledige methode](skills/innovatieploeg/README.md), gebruik [het vijfstappenwerkboek](examples/innovatieploeg-werkboek.md), bekijk [een doorlopend voorbeeld](examples/innovatieploeg-showbrief.md) of organiseer zelf [Innovatie in een dag](examples/innovatie-in-een-dag.md).

## Wat is een skill?

Een skill is een map met een `SKILL.md` en eventueel aanvullende referenties. Een compatibele AI-agent leest de beschrijving om te bepalen wanneer de skill nuttig is en gebruikt daarna de werkwijze uit het bestand.

De skills bevatten geen eigen model, verborgen prompt of betaalde koppeling. Ze leggen een herhaalbare manier van werken vast. Lees de inhoud altijd voordat je een skill installeert.

## Installeren zonder terminal

1. [Download de hele repository als ZIP](https://github.com/erwinblom/open-ai-skills-nl/archive/refs/heads/main.zip).
2. Pak het bestand uit en kies één skillmap, bijvoorbeeld `skills/tekstploeg/de-tegenlezer`.
3. Maak van die ene skillmap opnieuw een ZIP. Upload die ZIP naar een AI-omgeving die skills kan installeren of geef `SKILL.md` als projectinstructie mee.
4. Vraag de agent eerst de inhoud te controleren.

Mogelijke opdracht:

> Controleer en installeer de skill `de-tegenlezer` uit deze ZIP. Vertel daarna hoe ik hem in deze tool aanroep.

Kan je tool geen skills installeren? Open `SKILL.md`, voeg de inhoud als projectinstructie toe en begin je opdracht met: “Volg De Tegenlezer bij deze taak.”

## Installeren met een CLI

### Codex

Kopieer één skillmap naar je lokale Codex-skillsmap:

```bash
mkdir -p ~/.agents/skills
cp -R skills/tekstploeg/de-tegenlezer ~/.agents/skills/
```

Of installeer de hele Innovatieploeg:

```bash
mkdir -p ~/.agents/skills
cp -R skills/innovatieploeg/* ~/.agents/skills/
```

Codex detecteert wijzigingen automatisch. Noem de skill expliciet met `$`, bijvoorbeeld:

> Gebruik $de-tegenlezer om dit voorstel kritisch te beoordelen.

Zie [de uitgebreide installatiehandleiding](docs/installeren.md).

### Andere AI-tools

Dezelfde skillmappen zijn ook direct te gebruiken in onder meer:

- **Claude Code:** kopieer naar `~/.claude/skills/` of `.claude/skills/`;
- **Gemini CLI:** installeer met `gemini skills install` of kopieer naar `~/.gemini/skills/`;
- **GitHub Copilot in VS Code:** gebruik `.github/skills/`, `.claude/skills/` of `.agents/skills/`;
- **andere chat- en agenttools:** voeg `SKILL.md` en de gevraagde referentiebestanden als instructie of projectcontext toe.

Zie [Skills gebruiken buiten OpenAI](docs/installeren.md#andere-ai-tools).

## Aanroepen per tool

| Tool | Expliciete aanroep |
|---|---|
| ChatGPT | selecteer de skill met `@` |
| Codex | noem de skill met `$`, bijvoorbeeld `$de-tegenlezer` |
| Claude Code | gebruik `/de-tegenlezer` |
| Gemini CLI | vraag om de taak; Gemini activeert na toestemming de passende skill |
| GitHub Copilot in VS Code | gebruik de skill via Chat/Agent Skills |
| Gewone chattool | schrijf “Volg De Tegenlezer” en voeg `SKILL.md` als instructie toe |

## Zelf gebruiken

De voorbeelden hieronder gebruiken de Codex-notatie met `$`. Gebruik in ChatGPT `@`, in Claude Code `/` of in een gewone chattool de menselijke skillnaam.

Je hoeft geen speciale prompt te leren. Geef materiaal en doel mee:

```text
Gebruik $de-cliche-verwijderaar. Maak deze nieuwsbrief concreter,
maar behoud mijn directe toon en alle feiten.
```

```text
Gebruik $de-kansverkenner. Zoek drie kansen rond AI voor kleine
Nederlandse muziekpodia die met weinig vaste kosten te testen zijn.
```

```text
Gebruik $de-bewijsweger. Hier zijn de resultaten van onze pilot.
Moeten we doorgaan, aanpassen of stoppen?
```

## Grenzen

- Virtuele klanten zijn geen echte klanten en bewijzen geen koopgedrag.
- Een eerste versie is geen bewijs van een houdbaar bedrijf.
- AI kan fouten maken en bronnen verkeerd interpreteren.
- Controleer medische, juridische, financiële en reputatiegevoelige conclusies altijd met passende deskundigheid.
- Deel geen vertrouwelijke of persoonlijke gegevens zonder een veilige werkwijze en toestemming.

## Compatibiliteit

De installatie-instructies zijn gecontroleerd op **17 augustus 2026** aan de hand van de officiële documentatie voor [ChatGPT en Codex](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills), [Gemini CLI](https://geminicli.com/docs/cli/skills/) en [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills). Producten veranderen; meld verouderde instructies via een issue.

## Begeleiding

De skills zijn gratis te gebruiken en aan te passen. Voor teams die in korte tijd tot een resultaat willen komen, is er een begeleide aanpak:

**Innovatie in een dag** brengt één team rond één echte uitdaging van kans naar een testbare eerste versie. Daarna volgt echt klantonderzoek en kan De Bewijsweger bepalen wat de resultaten rechtvaardigen. [Open een issue](https://github.com/erwinblom/open-ai-skills-nl/issues) voor vragen over toepassing of begeleiding.

## Bijdragen

Verbeteringen en nieuwe voorbeelden zijn welkom. Lees [CONTRIBUTING.md](CONTRIBUTING.md). Nieuwe skills horen een afgebakende taak uit te voeren en mogen niet grotendeels overlappen met bestaande skills.

## Licentie

MIT. Je mag de skills gebruiken, aanpassen en verspreiden. Zie [LICENSE](LICENSE).

Gemaakt door [Erwin Blom](https://github.com/erwinblom).
