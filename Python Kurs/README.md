# Python Kurs ENT3R

**Selve Kurset ligger i mappen `src`**

Under følger en del instrukser for å kunne bruke koden på din egen maskin. Det er noen kommandoer du må kjøre i en terminal, jeg anbefaler at du bruker en editor som VScode eller lignende, men det er mulig å gjøre det samme med en helt vanlig terminal (som du brukte til å clone fra git). VScode har en terminal integrert, som du kan åpne ved å dra opp menyen fra den blå/lilla kanten i bunn og trykke på "Terminal" knappen.

## Starte virtual enviroment

Først av alt, naviger til riktig mappe. Hvis du bruker VScode burde du allerede være i riktig mappe, men dobbeltsjekk at det står `\ENT3R>` før der du kan skrive inn. Hvis ikke det står ENT3R der, så må du navigere til riktig mappe ved å bruke kommandoene for navigasjon som står i README filen i ENT3R mappen (som du klonet). Når du er i ENT3R mappen, så er det bare å kjøre kommandoen under for å gå inn i Python Kurs mappen.

```shell script
cd "Python Kurs"
```

Denne mappen er et python virtual enviroment, det betyr at det er mulig å laste ned pakker som matplotlib og numpy her, uten at det er lastet ned ellers på pc'en din.
Du trenger heller ikke ha python installert på pc'en. For å starte virtual enviroment er det bare å kjøre følgende kommando:

Windows:

```shell script
Scripts\activate.bat
```

Mac:

```shell script
./Scripts/activate
```

Etter dette skal det stå `(Python Kurs) C:\filbanen_din_her\ENT3R\Python Kurs>` i terminalen din hvis du er på windows, på mac ser det anderledes ut, men det skal fortsatt stå `(Python Kurs)` først.

Legg merke til at du må aktivere dette vertual enviroment hvis du åpner en ny terminal, hvis noe går galt dobbeltsjekk at det er aktivert ved å se om det står `(Python Kurs)` i terminalen.

## Kjøre filer

For å kjøre den første python fila bruk følgende kommando: (Kan tilpasses for å kjøre de andre filene)

windows:

```shell script
python src\basic_python\1_variabler.py
```

mac:

```shell script
python src/basic_python/1_variabler.py
```

Tips: Du kan trykke på tab for å autocomplete i terminalen, så bare skriv `python src\basi` og trykk på tab så står det `python src\basic_python`

Tips2: Hvis du trykker på pil opp i terminalen kan du gå gjennom kommandoer du nylig har skrevet inn

## VScode

Det kan hende VScode klager, i så fall pass på at VScode bruker riktig python installasjon. (Det følger med en python installasjon i dette virtual enviromentet)
Trykk `Crtl + shif + p` for å åpne command paletten, skriv `Python: Select Interpreter`, og trykk enter. Trykk på `+ Enter interpreter path` og trykk på `Find...`. Da skal du få åpnet file explorer i mappen `Python Kurs` eller `ENT3R`. Uansett er det bare å velge fila som ligger i `Python Kurs\Scripts\python.exe`.
