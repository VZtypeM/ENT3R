# Python Kurs ENT3R

Kurset ligger i mappen `src`

## Starte virtual enviroment

Først av alt sjekk at du er i riktig mappe, hvis du klonet hele repoet mitt må du først gå til mappen `Python Kurs` ved å kjøre kommandoen

```shell script
cd "Python Kurs"
```

Denne mappen er et python virtual enviroment, det betyr at det er mulig å laste ned pakker som matplotlib og numpy her uten at det er lastet ned ellers på pc'en din.
Du trenger heller ikke ha python installert på pc'en. For å starte virtual enviroment er det bare å kjøre følgende kommando fra mappen `Python Kurs`.

```shell script
Scripts\activate.bat
```

## Kjøre filer

Etter dette skal det stå `(Python Kurs) C:\filbanen_din_her\Python Kurs>` i terminalen din

For å kjøre den første python fila bruk følgende kommando: (Kan tilpasses for å kjøre de andre)

```shell script
python src\basic_python\1_variabler.py
```

Tips: Du kan trykke på tab for å autocomplete i terminalen, så bare skriv `python src\basi` og trykk på tab så står det `python src\basic_python`

## VScode

Det kan hende VScode klager, i så fall pass på at VScode bruker riktig python installasjon. (Det følger med en python installasjon i dette virtual enviromentet)
Trykk `Crtl + shif + p` for å åpne command paletten, skriv `Python: Select Interpreter`, og trykk enter. Trykk på `+ Enter interpreter path` og trykk på `Find...`. Da skal du få åpnet file explorer i mappen `Python Kurs` eller `ENT3R`. Uansett er det bare å velge fila som ligger i `Python Kurs\Scripts\python.exe`.
