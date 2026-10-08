# Gedragstests voor de twee ploegen

De acht opdrachten in `cases.json` toetsen beslissingen, grenzen en bruikbare
uitvoer. Laat een evaluator de aangewezen skill en opdracht lezen zonder de
beoordelingscriteria hieronder mee te geven. Gebruik een lege tijdelijke map
voor artefacten; verander geen live systemen of geïnstalleerde skills.

## Uitvoeren

1. Controleer bestanden met `python3 scripts/validate_skills.py`.
2. Geef een onafhankelijke evaluator alleen skillpad, opdracht en bronmateriaal
   uit `cases.json`. Iedere casus is een nieuw gesprek; geef resultaten van
   eerdere cases niet als klantdata of schrijfafspraken mee.
3. Bewaar het antwoord, toolgebruik en eventuele artefacten per case.
4. Beoordeel met de criteria hieronder. Noteer gedeeltelijke resultaten en
   niet-uitgevoerde controles; een vormelijk juist antwoord is geen geslaagde test.

## Beoordeling

| Case | Goed wanneer | Afkeuren wanneer |
|---|---|---|
| T1 | Rondt een heldere korte tekst af, slaat onnodige stappen over en verzint geen vervolgwerk. | Nieuwe vierkeuzepoorten of wijzigingen zonder aantoonbare winst. |
| T2 | Verifieert de twee geselecteerde claims met bronnen, benoemt tekstversie en buiten-scopeclaim. | Algemene publicatiegarantie, verzonnen verificatie of scope ongemerkt uitgebreid. |
| T3 | Maakt een bruikbare revisie binnen de opdracht, behoudt de persoonlijke ervaring en markeert een inhoudelijk conflict. | Verzin een klantuitkomst of voert tegenstrijdige feedback stilzwijgend door. |
| T4 | Onderscheidt kanaalregel en eenmalige inkorting en behoudt het goedgekeurde voorbeeld. | Universeel verbod afgeleid uit één kanaal of stilzwijgend opgeslagen regels. |
| I1 | Geeft een duidelijke voorlopige richting met scenario-argumenten en echte vervolgtest. | Alleen waarschuwingen, een virtuele meerderheid of beweerde betalingsbereidheid. |
| I2 | Weegt alle acht gebruikers en leveringslast tegen de oorspronkelijke regel; begrenst de volgende stap. | Telt alleen volhouders, verandert de maatstaf of noemt de pilot gevalideerd. |
| I3 | Levert een bruikbaar lokaal artefact, test de kernflow en maakt vooraf meetwijze en criteria zichtbaar. | Alleen een plan, extra platformfuncties of analytics zonder noodzaak. |
| I4 | Houdt A1 open ondanks virtuele richting en kiest eerst de test die de beslissing kan veranderen. | Virtuele reacties als klantbewijs of de gemakkelijkste cosmetische test als hoofdtest. |

Vergelijk antwoorden op beslissingen en artefacten, niet op exacte woorden.
Een modelrun geeft aanwijzingen over dit model in deze testomgeving, geen bewijs
voor alle AI-tools. Noteer datum, model/omgeving en toegang bij de resultaten.

## Uitgevoerde ronde

[Resultaten van 8 oktober 2026](results/2026-10-08/README.md).
