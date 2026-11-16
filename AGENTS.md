# Skills aanpassen: instructies voor de AI

Je helpt iemand die een skill uit de Tekstploeg of Innovatieploeg naar eigen werk wil vormen, of een eigen ploeg wil samenstellen. Ga ervan uit dat die persoon geen programmeur is. Een skill is tekst; er is geen code nodig om hem te veranderen.

## Hoe je werkt

- Maak een kopie van de skillmap met een eigen naam. Het origineel blijft staan.
- Verander ook de `name` bovenaan `SKILL.md` van de kopie, zodat beide versies naast elkaar bruikbaar zijn.
- Verander één ding per keer, zo klein als kan.
- Leg in gewone taal uit wat je hebt veranderd en geef een opdracht waarmee de gebruiker het verschil kan testen.
- Publiceer of verstuur niets.

## Waar alles staat

| Wat | Waar |
|---|---|
| De negen skills van de Tekstploeg | `skills/tekstploeg/<naam>/SKILL.md` |
| De vijf skills van de Innovatieploeg | `skills/innovatieploeg/<naam>/SKILL.md` |
| Naslag die bij een skill hoort | de map `references` in de skillmap |
| Uitleg per ploeg | `skills/tekstploeg/README.md` en `skills/innovatieploeg/README.md` |
| Voorbeelden, waaronder een uitgewerkte aanpassing | `examples/` |
| Installeren per AI-tool | `docs/installeren.md` |
| De Tekstploeg als plugin | `plugins/de-tekstploeg` (een kopie van de skills) |

Een `SKILL.md` begint met `name` en `description`. De `description` bepaalt wanneer een AI-tool de skill uit zichzelf inzet. Houd die concreet als je de taak van een skill verandert.

## Vrij te veranderen

Vragen, rollen, stappen, de vorm van het resultaat, de toon, de taal, welke skills bij een ploeg horen. Skills weghalen, samenvoegen of toevoegen mag. Er zijn geen heilige prompts.

## Wat heel moet blijven

1. **Eerlijkheid over bewijs.** De skills maken onderscheid tussen wat gecontroleerd is en wat niet, en verzinnen geen bronnen, citaten of klantreacties. Haal die grenzen niet weg om een vlotter resultaat te krijgen.
2. **De gebruiker beslist.** De skills van de Tekstploeg laten de gebruiker kiezen tussen voor mij, met mij, zelf doen of overslaan. Verwijder die keuze alleen als de gebruiker dat vraagt.
3. **Geen verborgen afhankelijkheden.** Geen betaalde dienst, sleutel of account dat de gebruiker niet zelf heeft gekozen.
4. **`LICENSE` en de naam van de maker** blijven bij wat je deelt.

## Controleren na elke wijziging

1. Laat de gebruiker de aangepaste skill en het origineel dezelfde opdracht geven en de uitkomsten vergelijken.
2. Draai `python3 scripts/validate_skills.py` als Python beschikbaar is. Dat controleert de opbouw van de skills.
3. Verander je een skill van de Tekstploeg in deze repository zelf, werk dan ook de kopie in `plugins/de-tekstploeg` bij. De controle meldt het als die twee uit elkaar lopen.

## Een eigen versie delen

De skills vallen onder MIT. Wie een aangepaste ploeg deelt, bewaart de licentie en de vermelding van Erwin Blom, en geeft de eigen versie een eigen naam.
