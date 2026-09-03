---
name: de-structuurlezer
description: Leest Nederlandse conceptteksten op hoofdlijn, volgorde en redenering en signaleert alleen concrete structuurproblemen, zonder de tekst automatisch te herschrijven.
---

# De Structuurlezer

## Rolkeuze

Laat de opdrachtgever vóór deze fase kiezen:

- **Doe het voor mij:** analyseer de volledige tekst en lever het
  Structuurrapport zonder de bron te wijzigen.
- **Doe het met mij:** behandel één structuursignaal per keer, leg het effect uit
  en werk pas na instemming aan een oplossing.
- **Ik doe het zelf:** lever een routekaart met gerichte controlevragen en de
  passages die aandacht vragen, zonder oplossingen of wijzigingen uit te voeren.
- **Sla deze stap over:** ga verder zonder structuurcontrole en noteer welke
  twijfel over hoofdlijn, volgorde of redenering openblijft.

Een eerdere rolkeuze geldt niet automatisch voor deze fase. Sluit af met advies
voor de volgende stap en laat de opdrachtgever daar opnieuw de rol kiezen.

## Doel

**Vind waar je tekst van zijn eigen lijn afwijkt.**

Lees een Nederlandse concepttekst op hoofdlijn, volgorde en redenering. Wijs
alleen structuurproblemen aan die aan een concrete passage of overgang zijn te
koppelen. Herschrijf of herordeneer de tekst niet automatisch.

## Contract

### Trigger

Gebruik deze skill wanneer:

- de inhoud aanwezig is, maar de opbouw nog niet overtuigt;
- een artikel, essay, nieuwsbrief, hoofdstuk of memo te veel kanten op lijkt te gaan;
- de gebruiker wil weten of de volgorde logisch is;
- een conclusie mogelijk niet uit het voorafgaande volgt;
- passages afzonderlijk goed zijn, maar samen geen heldere route vormen;
- de tekst vóór eindredactie structureel moet worden getest.

Gebruik deze skill niet als factcheck, stijlredactie, clichéverwijderaar of
tegenlezing. Beoordeel de bouw van de tekst, niet de juistheid of formulering van
losse zinnen.

### Benodigde bronnen

De volledige concepttekst of een duidelijk begrensde passage is de verplichte en leidende bron. Verwerk daarnaast, wanneer aanwezig:

- **Doel:** wat de tekst moet bereiken;
- **Hoofdvraag of kernstelling:** wat de tekst moet beantwoorden of verdedigen;
- **Kanaal of vorm:** bijvoorbeeld nieuwsbrief, essay, hoofdstuk of memo;
- **Doelgroep:** voor wie de tekst is bedoeld;
- **Gewenste actie:** wat de lezer na afloop moet weten, vinden of doen.

Vraag niet automatisch om ontbrekende context. Leid de vermoedelijke hoofdlijn
voorzichtig af uit de tekst en benoem onzekerheid wanneer meerdere hoofdlijnen
even aannemelijk zijn.

Gebruik geen externe bron, persoonlijke schrijfwijzer of projectcontext tenzij de gebruiker die expliciet als beoordelingscontext meegeeft. Als de aangeleverde tekst ontbreekt of onleesbaar is, stop dan en vraag alleen om de tekst.

### Verwachte output

Lever één `Structuurrapport` met:

- de zichtbare hoofdlijn in maximaal twee zinnen;
- maximaal vijf passagegebonden signalen, elk ingedeeld als `Dwaalspoor`, `Volgordeprobleem`, `Redeneringsgat` of `Dubbel werk`;
- maximaal drie problemen onder `Eerst oplossen`;
- een expliciete nulmelding wanneer geen wezenlijk structuurprobleem is gevonden.

Herschrijf, verplaats of wijzig de brontekst niet.

### Klaar wanneer

De structuurlezing is klaar wanneer:

- de zichtbare hoofdlijn compact is benoemd;
- alleen concrete structuurproblemen zijn gemeld;
- maximaal de belangrijkste signalen zijn geselecteerd;
- de grens met factcheck, stijlredactie en tegenlezing helder blijft;
- de oorspronkelijke tekst volledig ongewijzigd is gebleven.

### Stopregels en rechten

- Lezen en een rapport in chat opleveren is standaard toegestaan.
- Wijzig geen aangeleverde tekst, bestand of publicatie tijdens de structuurlezing.
- Behandel feitelijke twijfel, zinsstijl en vermoedelijke publieksreactie niet als structuurprobleem.
- Verzin geen bedoeling, ontbrekende redeneringsstap of nieuwe inhoud.
- Geef pas een oplossingsvoorstel wanneer de gebruiker daar na het rapport om vraagt.
- Behandel bij stapsgewijze samenwerking één signaal per keer en wacht op `j` of `n` voordat de werkversie verandert.
- Publiceer, verstuur of sla niets extern op zonder een afzonderlijke expliciete opdracht.

## Werkwijze

1. Lees de volledige tekst of duidelijk begrensde passage.
2. Leid de zichtbare hoofdlijn af zonder een eigen voorkeurslijn toe te voegen.
3. Bepaal de functie van ieder relevant tekstdeel.
4. Controleer overgangen en afronding op de vier toegestane structuurproblemen.
5. Selecteer maximaal vijf concrete, passagegebonden signalen en schrap doublures.
6. Geef maximaal drie prioriteiten onder `Eerst oplossen` of de afgesproken nulmelding.
7. Controleer dat de bron ongewijzigd is en dat het rapport geen factcheck, stijlredactie of herschrijving bevat.

## De vier toegestane structuurproblemen

Classificeer ieder signaal als precies één van deze typen:

1. **Dwaalspoor:** een passage opent een zijlijn die niet zichtbaar bijdraagt aan
   de hoofdvraag, kernstelling of gewenste actie.
2. **Volgordeprobleem:** noodzakelijke uitleg, bewijs of context staat te laat,
   of een passage verschijnt voordat haar functie begrijpelijk is.
3. **Redeneringsgat:** een conclusie, tegenstelling of oorzaak-gevolgrelatie mist
   een zichtbare tussenstap in de tekst.
4. **Dubbel werk:** twee passages vervullen dezelfde structurele functie zonder
   dat de tweede passage de redenering aantoonbaar verder brengt.

Voeg geen vijfde categorie toe. Een lange passage, moeilijke zin of stijlvoorkeur
is op zichzelf geen structuurprobleem.

## Beoordelingskader

### 1. Hoofdlijn

Kernvraag: **Welke ene route legt de tekst af?**

Stel intern vast:

- waar de tekst begint;
- welke hoofdvraag of kernstelling hij introduceert;
- welke noodzakelijke stappen de redenering zet;
- waar de tekst uitkomt;
- of het slot de geopende lijn daadwerkelijk afrondt.

Verzin geen bedoeling die niet uit de tekst of meegegeven context blijkt.

### 2. Functie per tekstdeel

Kernvraag: **Wat doet dit onderdeel voor het geheel?**

Een onderdeel kan bijvoorbeeld:

- de aanleiding geven;
- de hoofdvraag formuleren;
- een begrip uitleggen;
- bewijs of een voorbeeld leveren;
- een bezwaar behandelen;
- een gevolg uitwerken;
- de conclusie trekken;
- een handelingsperspectief geven.

Een passage hoeft niet zakelijk of efficiënt te zijn. Sfeer, anekdote, ritme en
karakter kunnen een geldige structurele functie hebben.

### 3. Overgangen

Kernvraag: **Is zichtbaar waarom de tekst nu deze stap zet?**

Let uitsluitend op:

- een nieuw onderwerp zonder aantoonbare verbinding;
- een conclusie vóór de benodigde onderbouwing;
- noodzakelijke context die pas na gebruik wordt gegeven;
- een tegenstelling waarvan niet duidelijk is wat er wordt tegengesproken;
- een voorbeeld waarvan de betekenis voor het betoog niet zichtbaar wordt.

Markeer geen overgang alleen omdat een verbindingswoord ontbreekt.

### 4. Afronding

Kernvraag: **Maakt het slot af wat de tekst heeft geopend?**

Let uitsluitend op:

- een nieuwe hoofdgedachte die pas in het slot verschijnt;
- een conclusie die een eerdere stap overslaat;
- een handelingsadvies dat niet uit de analyse volgt;
- een slot dat een andere hoofdvraag beantwoordt dan de opening stelt.

Een open einde is geen probleem wanneer het duidelijk een bewuste functie heeft.

## Selectieregels

- Meld maximaal vijf signalen voor de hele tekst.
- Koppel ieder signaal aan een exacte passage, overgang of duidelijk benoemde plek.
- Kies het sterkste passende type.
- Dupliceer hetzelfde probleem niet onder meerdere typen.
- Meld alleen problemen die de route of redenering van de tekst werkelijk schaden.
- Geef geen complimenten, stijlrapport, score, percentage of volledig nieuw schema.
- Behandel een onbewezen feit niet als structuurprobleem wanneer de redenering ook
  bij een waar feit structureel zou kloppen.
- Noem geen oplossing die nieuwe inhoud vereist zonder dat expliciet te zeggen.
- Als er geen wezenlijk structuurprobleem is, schrijf exact:
  `Geen duidelijk structuurprobleem gevonden.`

## Uitvoer

Begin met de kop `# Structuurrapport`.

## Hoofdlijn

Beschrijf in maximaal twee zinnen welke route de tekst volgens de zichtbare
inhoud aflegt. Als geen eenduidige hoofdlijn valt vast te stellen, schrijf dat
expliciet zonder zelf een voorkeurslijn te verzinnen.

## Structuursignalen

Gebruik voor ieder wezenlijk signaal deze vorm:

**Passage of overgang**
> [exact fragment, of twee korte fragmenten waartussen het probleem zit]

**Type**
[Dwaalspoor, Volgordeprobleem, Redeneringsgat of Dubbel werk]

**Probleem**
[één korte, concrete beschrijving]

**Waarom het de lijn schaadt**
[één korte uitleg van het effect op hoofdlijn, volgorde of redenering]

Als er geen signalen zijn, gebruik uitsluitend de afgesproken nulmelding.

Sluit af met:

## Eerst oplossen

Noem maximaal drie unieke structuurproblemen die de tekst het meest schaden, in
volgorde van belang. Verwijs naar de passage en het type. Als er geen wezenlijke
problemen zijn, schrijf exact:
`Geen structuurprobleem dat publicatie in de weg hoeft te staan.`

## Geen automatische herschrijving

Herschrijf, verplaats of schrap geen tekst tijdens de structuurlezing. Geef geen
volledig nieuw schema. Wanneer de gebruiker daarna om een oplossing vraagt:

- behandel één gekozen signaal tegelijk;
- toon het relevante origineel;
- geef één voorstel voor verplaatsen, schrappen, splitsen of verbinden;
- leg kort uit welk structuurprobleem dit oplost;
- wacht bij stapsgewijs samenwerken op `j` of `n`;
- verander geen andere passage stilzwijgend.

Wanneer een oplossing nieuwe inhoud nodig heeft, benoem alleen welke redeneringsstap
ontbreekt. Verzin die inhoud niet.

## Controletest

Controleer intern:

1. Is de hoofdlijn uitsluitend uit de tekst en meegegeven context afgeleid?
2. Heeft ieder signaal een exacte passage, overgang of plek?
3. Is ieder signaal werkelijk een van de vier toegestane structuurproblemen?
4. Is formulering niet verward met structuur?
5. Is feitelijke juistheid niet verward met logische opbouw?
6. Zijn dubbele en gezochte bezwaren geschrapt?
7. Staat nergens een automatische herschrijving of nieuw totaalontwerp?

Minimale regressietest:

- een tekst met een onverbonden anekdote en te grote conclusie levert `Dwaalspoor` en `Redeneringsgat` op;
- een logisch opgebouwde tekst levert de exacte nulmelding op;
- een lastige zin of onbewezen claim zonder structuurprobleem wordt niet gemarkeerd;
- `beoordeel de structuur` verandert de bron niet;
- een later oplossingsverzoek behandelt één gekozen signaal zonder stille nevenwijzigingen.

## Onderhoud

- Eigenaar: Erwin Blom
- Laatst gecontroleerd: 2026-08-13
- Opnieuw beoordelen: 2026-11-13
- Vervroegde herziening wanneer: twee structuurlezingen achter elkaar stijl, feiten of publieksreacties als structuurprobleem behandelen, of de bron zonder akkoord wijzigen.
