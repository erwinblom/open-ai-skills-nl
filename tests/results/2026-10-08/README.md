# Gedragscontrole — 8 oktober 2026

De twee collecties zijn getoetst door twee afzonderlijke Codex-subagents, één
per ploeg. Zij lazen de skillinstructies en opdrachten, zonder deze
beoordelingscriteria of de wijzigingen te zien. Per casus was de opdracht
zelfstandig; de vier casussen per ploeg deelden wel dezelfde agentcontext. De
modelidentificatie is niet apart vastgelegd. Dit is een beperkte praktijkproef,
geen benchmark of bewijs voor alle modellen en AI-tools.

De tekst-evaluator zag bij het inlezen ook de innovatieopdrachten, maar gebruikte
die niet. De eigenlijke beoordelingscriteria bleven buiten de evaluatiecontext.
De primaire Python-documentatie was voor T2 bereikbaar. Bestandswijzigingen en
artefacten bleven buiten gebruikersdata en live systemen.

| Case | Beoordeling | Waarneming |
|---|---|---|
| [T1](T1.md) | Geslaagd | Korte zelfstandige redactie zonder extra rolkeuze of volledige controleketen. |
| [T2](T2.md) | Geslaagd | Twee claims onderbouwd met officiële documentatie; concept v2 en derde claim buiten scope benoemd. |
| [T3](T3.md) | Geslaagd | Dubbele feedback gebundeld, strijdig slotadvies benoemd en het opgegeven standpunt behouden. |
| [T4](T4.md) | Geslaagd | LinkedIn-regel met citaatuitzondering, festivalnaam als eenmalige inkorting; niets blijvend opgeslagen. |
| [I1](I1.md) | Geslaagd | Virtuele perspectieven geven een concrete voorlopige richting B en een echte vervolgtest. |
| [I2](I2.md) | Geslaagd | Alle acht deelnemers blijven in de noemer; 2/8 zelfstandig gebruik haalt het criterium 5/8 niet. Volgende stap maximaal vier uur. |
| [I3](I3.md) | Geslaagd | Vooraf meetplan, werkende lokale HTML en negen geslaagde browsercontroles. Echte gebruikersproef nog niet uitgevoerd. |
| [I4](I4.md) | Geslaagd | Echte aanlevering krijgt voorrang boven de logotest; virtuele richting verandert de bewijsstatus van A1 niet. |

De instructie- en metadata-controle slaagt voor alle veertien skills; de
pluginbestanden zijn gelijk aan de losse Tekstploeg-skills. Deze controles
bewijzen op zichzelf geen goed gedrag. Onbereikbare bronnen, alle individuele
rollen, alle mogelijke revisielussen en andere AI-tools zijn niet afzonderlijk
met deze ronde afgedekt.

Bij I3 zijn het [testartefact](facturen.html), [browsercontrolebewijs](kernflowcontrole.json)
en desktop-/mobielbeelden bewaard. Het HTML-bestand is uitsluitend uitvoer van
deze test, geen extra product. De oorspronkelijke browsercontrole draaide op
een tijdelijk lokaal pad dat in het bewijsbestand staat; de meegeleverde kopie
bevat hetzelfde artefact. De sandboxstart mislukte, waarna een toegestane start
buiten de sandbox slaagde. Er zijn geen echte pilotdeelnemers getest.

Na de proef zijn uitsluitend de beschrijving en twee bestaande passages van De
Klantverkenner in lijn gebracht met de al geteste richtingsfunctie; de werkwijze
en beslisgrenzen bleven gelijk. Deze tekstuele verduidelijking is niet opnieuw
met een agent beproefd.
