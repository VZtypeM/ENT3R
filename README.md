# ENT3R

Dette er en mappe som inneholder noen prosjekter i tilknytning til deltidsjobben min i ENT3R.

Det er bare å klone denne mappa og teste ut koden selv, du kan endre ting lokalt, men det er ikke mulig å endre ting på denne siden. (Bør ikke være det ihvertfall)

## Hvorfor klone og ikke bare kopiere?

Det er ikke mye vits i å klone hvis ikke du har tenkt til å eksperimentere og kjøre koden jeg har skrevet på egen maskin, men hvis du kloner får du kopiert alle filene til datamaskinen din. For python kurs mappa følger det også med en hel installasjon av python 3.10 og alle biblioteker som trengs. Dette er ikke noe du får uten å kopiere alle de 4 000 små filene i `Python Kurs/Lib/site-packages` mappa. (Bare gjør det for hånd, no problem)

Ved å klone får du altså satt opp python på datamaskinen din til å kunne kjøre pylab, slik elevene lærer om og kommer til å ha spørsmål til.

## Hvordan å klone

1. Åpne terminalen
   - På windows åpne start menyen og søk på "cmd" og trykk enter da skal terminalen åpnes i hjem mappa di.
   - Hvis du ikke vet hvordan du gjør det på mac, så søk etter "Open terminal mac" på google
2. Naviger til riktig mappe. Dette punktet kan hoppes over hvis du synes det er greit å laste ned i hjem mappa di. Skriv in `cd din_mappe_her` for å bytte til en mappe (både windows og mac) og skriv `dir` (windows) eller `ls` (mac) for vise hvilke mapper som finnes der du er nå. `cd ..`betyr gå til mappa ovenfor.
3. Når du er i riktig mappe skriv inn følgende kommando i terminalen:

   ```shell scipt
   git clone https://github.com/VZtypeM/ENT3R.git
   ```

   (Hvis du lurer så er linken over kopiert fra den grønne knappen på denne siden)
   Hvis det står at `'git' is not recognized as an internal or external command, operable program or batch file.` eller noe som ligner, så betyr det at du ikke har git installert. Bare søk "install git windows" og følg instruksjonene.

4. Nå har du klonet prosjektet! Neste steg er å åpne prosjektet med f. eks. VScode og gå inn i mappen `Python Kurs`. Der finner du en README fil med flere instruksjoner på hva du må gjøre for å kjøre koden.
