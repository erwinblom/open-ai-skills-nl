---
name: de-schrijfwijzer
description: Haalt herbruikbare lessen uit een Nederlandse schrijfronde door opdracht, versies en feedback te vergelijken en stelt gerichte wijzigingen voor aan stem-, project- en werkafspraken zonder incidentele keuzes automatisch tot vaste regels te maken.
---

# De Schrijfwijzer

## Doel

Zorg dat feedback op een tekst bruikbaar wordt voor volgende teksten. Vergelijk
de opdracht, eerdere versie, ontvangen feedback en eindversie. Zoek alleen
lessen die aantoonbaar herbruikbaar zijn en houd persoonlijke stem,
projectafspraken en eenmalige keuzes uit elkaar.

## Contract

### Trigger

Gebruik deze skill wanneer:

- een tekst na feedback of redactie is afgerond;
- iemand wil vastleggen wat een schrijfronde heeft geleerd;
- dezelfde correctie vaker terugkomt;
- een bestaande `VOICE.md`, `STYLE.md`, schrijfwijzer of projectinstructie moet
  worden verbeterd op basis van werkelijk schrijfwerk;
- eerste en laatste versie moeten worden vergeleken om blijvende voorkeuren te
  vinden.

Gebruik deze skill niet als gewone stijlredactie, factcheck, structuurlezing of
tegenlezing. De skill beoordeelt het leerproces tussen versies en maakt niet
zelfstandig een nieuwe eindversie.

### Benodigde bronnen

Gebruik minimaal twee van deze bronnen:

- oorspronkelijke opdracht of briefing;
- eerste of eerdere tekstversie;
- concrete feedback, correcties of afgewezen voorstellen;
- goedgekeurde eindversie;
- bestaande stem-, stijl- of projectafspraken.

De sterkste basis is een eerdere versie plus de goedgekeurde eindversie en de
feedback die de verandering verklaart. Als alleen een eindtekst beschikbaar is,
kan de skill voorbeelden signaleren, maar geen betrouwbare leerregel afleiden.

Vraag alleen om ontbrekend materiaal wanneer zonder dat materiaal geen verschil
of feedbackbesluit kan worden vastgesteld. Behandel stilte of het accepteren van
een AI-voorstel niet automatisch als instemming.

### Verwachte output

Lever standaard een `Leerredactierapport` met:

1. **Wat veranderde:** maximaal vijf betekenisvolle verschillen;
2. **Wat daarvan herbruikbaar is:** alleen lessen met zichtbare onderbouwing;
3. **Waar de les thuishoort:** `Stem`, `Project`, `Werkwijze` of `Eenmalig`;
4. **Voorgestelde regel:** kort, concreet en positief uitvoerbaar;
5. **Bewijs:** passages, feedback of herhaling waarop de regel rust;
6. **Zekerheid:** `Sterk`, `Aannemelijk` of `Voorlopig`;
7. **Te behouden voorbeeld:** hooguit drie passages die als positief voorbeeld
   nuttiger zijn dan een abstracte regel;
8. **Besluitlijst:** `Vastleggen`, `Nog één keer toetsen` of `Niet bewaren`.

Schrijf voorgestelde regels zo dat een andere schrijver of agent ze kan
toepassen. Vermijd vage regels als “schrijf scherper” of “maak het menselijker”.

### Klaar wanneer

- iedere voorgestelde les terug te voeren is op aangeleverd materiaal;
- persoonlijke stem, projectvorm, proces en incident van elkaar zijn gescheiden;
- tegenstrijdige feedback zichtbaar blijft;
- bestaande regels niet onnodig worden verdubbeld;
- de gebruiker kan kiezen wat blijvend wordt vastgelegd;
- geen bronbestand zonder expliciete opdracht is gewijzigd.

### Stopregels en rechten

- Maak standaard alleen een rapport en wijzig geen bestanden.
- Vraag toestemming voordat voorgestelde lessen in bestaande bestanden worden
  verwerkt, tenzij de gebruiker in dezelfde opdracht expliciet om die wijziging
  vraagt.
- Toon bij een wijziging eerst welke regels worden toegevoegd, aangescherpt,
  vervangen of verwijderd.
- Bewaar geen volledige vertrouwelijke tekst als stijlvoorbeeld wanneer een
  korte passage of geanonimiseerde regel volstaat.
- Publiceer, verstuur, commit of push niets zonder afzonderlijke expliciete
  opdracht.

## Werkwijze

1. Bepaal welke versie door de schrijver als eindversie is goedgekeurd.
2. Vergelijk opdracht, versies en feedback op betekenis, structuur, toon,
   formulering en werkwijze.
3. Negeer mechanische wijzigingen zonder toekomstige waarde, zoals herstelde
   tikfouten en gewijzigde actualiteit.
4. Koppel ieder belangrijk verschil aan expliciete feedback of een duidelijke
   keuze in de eindversie.
5. Classificeer de mogelijke les:
   - `Stem`: een voorkeur die over projecten heen bij de schrijver hoort;
   - `Project`: een afspraak voor één publicatie, merk, genre of publiek;
   - `Werkwijze`: een betere volgorde, controle of samenwerking;
   - `Eenmalig`: een keuze die alleen bij deze tekst of situatie hoort.
6. Controleer bestaande afspraken op overlap of tegenspraak.
7. Ken zekerheid toe en formuleer de kleinste bruikbare regel.
8. Stel vastleggen alleen voor als de les voldoende bewijs heeft.

## Bewijsregels

Gebruik `Sterk` wanneer de schrijver een voorkeur expliciet als blijvend noemt,
of wanneer dezelfde correctie in meerdere teksten of rondes terugkomt.

Gebruik `Aannemelijk` wanneer één duidelijke correctie wordt bevestigd door de
goedgekeurde eindversie en past bij bestaande voorbeelden of afspraken. Adviseer
deze regel nog één keer te toetsen.

Gebruik `Voorlopig` bij één impliciete keuze, een door de AI voorgestelde
wijziging zonder expliciete reactie, of een verschil dat ook inhoudelijk of
situationeel kan zijn. Leg dit niet als vaste regel vast.

Een expliciete afwijzing is ook leerdata. Leg vast wat moet worden vermeden als
de reden duidelijk en herbruikbaar is. Formuleer waar mogelijk tevens het
gewenste alternatief.

Maak geen meerderheidsoordeel van tegenstrijdige feedback. Benoem het conflict
en vraag welke regel leidend is wanneer dit toekomstige teksten wezenlijk
verandert.

## Opslagadvies

Als de gebruiker met bestanden werkt, adviseer deze verdeling:

- persoonlijke en projectoverstijgende voorkeuren in `VOICE.md` of een
  persoonlijke schrijfwijzer;
- kanaal-, merk-, genre- en publieksafspraken in `STYLE.md` of de projectmap;
- procesafspraken in de relevante skill, route of werkwijze;
- sterke goedgekeurde passages bij de voorbeelden, met voldoende context om te
  begrijpen wat ze aantonen.

Voeg een nieuwe regel alleen toe wanneer een bestaande regel niet kan worden
aangescherpt. Bewaar voorbeelden vanwege het gedrag dat ze tonen, niet vanwege
het onderwerp waarover ze gaan.

## Uitvoer

Begin met `# Leerredactierapport`.

Gebruik voor iedere mogelijke les:

**Verschil**
> [korte passage uit eerdere versie] → [korte passage uit eindversie]

**Aanleiding**  
[expliciete feedback, afwijzing, keuze of herhaald patroon]

**Categorie**  
[Stem, Project, Werkwijze of Eenmalig]

**Voorgestelde regel**  
[één concrete, herbruikbare instructie, of `Geen regel vastleggen`]

**Zekerheid**  
[Sterk, Aannemelijk of Voorlopig]

**Besluit**  
[Vastleggen, Nog één keer toetsen of Niet bewaren]

Sluit af met `## Voorgestelde wijzigingen`. Toon daar per bestaand bestand de
exacte toevoeging, aanscherping of verwijdering. Schrijf `Nog niets wijzigen`
wanneer geen les sterk genoeg is of de gebruiker alleen om analyse vroeg.

## Controletest

Een schrijver vervangt in één nieuwsbrief “een fundamentele transformatie” door
“een verandering” en zegt: “Ik wil nooit van die opgepompte AI-taal.” Dezelfde
voorkeur staat al in zijn schrijfwijzer. Verwacht: `Stem`, zekerheid `Sterk`, de
bestaande regel aanscherpen met dit positieve voorbeeld en geen dubbele regel
toevoegen.

In dezelfde tekst wordt een festivalnaam ingekort omdat de volledige naam al in
de kop staat. Verwacht: `Eenmalig`, `Geen regel vastleggen` en `Niet bewaren`.
