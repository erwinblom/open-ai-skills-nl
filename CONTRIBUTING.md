# Bijdragen

Verbeteringen, foutmeldingen en nieuwe voorbeelden zijn welkom.

## Een bestaande skill verbeteren

1. Beschrijf welk concreet gedrag nu onvoldoende werkt.
2. Voeg een realistisch voorbeeld toe waarmee het probleem zichtbaar wordt.
3. Pas de kleinste hoeveelheid instructie aan die het probleem oplost.
4. Controleer dat de skill nog steeds zelfstandig en algemeen bruikbaar is.
5. Draai `python3 scripts/validate_skills.py`.

## Een nieuwe skill voorstellen

Een nieuwe skill moet:

- één herkenbare taak uitvoeren;
- een duidelijke aanleiding hebben om automatisch gebruikt te worden;
- voldoende verschillen van bestaande skills;
- zonder verborgen betaalde afhankelijkheden bruikbaar zijn;
- onzekerheid, veiligheid en grenzen eerlijk behandelen;
- minimaal één realistisch gebruiksvoorbeeld hebben.

Begin bij voorkeur met een issue waarin je beschrijft:

- wat iemand aan de skill vraagt;
- welk resultaat de skill oplevert;
- waarom een algemene AI-opdracht daarvoor onvoldoende is;
- bij welke collectie de skill hoort.

## Structuur

Iedere skillmap bevat minimaal:

```text
skillnaam/
├── SKILL.md
└── agents/
    └── openai.yaml
```

Voeg `references/` alleen toe voor informatie die niet bij iedere opdracht geladen hoeft te worden. Plaats handleidingen en demonstraties voor mensen in de centrale `docs/`- of `examples/`-map, niet in de skillmap.

## Schrijfstijl

- Schrijf in helder Nederlands.
- Gebruik directe instructies.
- Vermijd managementtaal en opgeblazen claims.
- Voeg geen lange uitleg toe die een goede AI-agent zelf kan afleiden.
- Maak duidelijk wat feit, inferentie en aanname is wanneer dat relevant is.

Door een bijdrage in te dienen, ga je ermee akkoord dat deze onder de MIT-licentie van het project wordt gepubliceerd.
