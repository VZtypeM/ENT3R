# I en if else setning vil alltid nøyaktig en av printene kjøre
# Hvis man bare har if og elif kan det hende ingen kjører

# Pass på forskjellen mellom = og ==
# = betyr sett variabelen til venstre lik verdien til høyre
# == betyr sjekk om verdiene til høyre og venstre er like

print(6 * 7 < 42)
print(6 * 7 == 42)
print(6 * 7 > 42)

if 6 * 7 < 42:
    print("6*7 er mindre enn 42")
elif 6 * 7 == 42:
    print("6*7 er akkurat 42")
else:
    print("6*7 er større enn 42")

# Legg merke til at når man har kolon ":" i python, så forventes det at man hopper inn et hakk på neste linje
# Alt som ligger på samme nivå eller mer til høyre inntil man hopper tilbake er en del av samme blokk
# For eksempel:
# Alle linjene fra og med 25 til og med 29 under er en del av blokken som kjøres hvis 3 < 7 på linje 24

if 7 < 3 or 2 == 1:
    print("7 er mindre enn 3 ELLER 2 er lik 1")
    if 0 != 1:
        print("0 er ikke lik 1")
    else:
        print("0 er lik 1")
else:
    print("7 er IKKE mindre enn 3 OG 2 er ikke lik 1")
