# range fungerere akkurat som en liste, men python bruker bare et tall om gangen i range (sparer tid og minne)
for variabel_navn in range(5):
    print(variabel_navn, end=" ")

# \n inni text betyr en ny linje
print("\n")


# Legg merke til at denne for loopn gjør akkurat det samme som den forrige (men den er mindre effektiv)
for variabel_navn in [0, 1, 2, 3, 4]:
    print(variabel_navn, end=" ")

print("\n")


# Fra og med -2, til (men ikke med) 10, øk med 2 hver gang:
for partall in range(-2, 10, 2):
    print(partall, end=" ")

print("\n")


# Fra og med 7, til (men ikke med) 0, øk med -1 hver gang:
for bakover in range(7, 0, -1):
    print(bakover, end=" ")

print("\n")


# Denne gjør også det samme som den første løkka
variabel_navn = 0
while variabel_navn < 5:
    print(variabel_navn, end=" ")
    variabel_navn += 1
# while kan brukes til alle løkker, for kan bare brukes når man vet hvor mange ganger løkka skal kjøre

print("\n")


# En annen måte å gjøre den første løkka på
variabel_navn = 0
while True:
    if variabel_navn >= 5:
        # break gjør at man hopper ut av løkka
        break
    print(variabel_navn, end=" ")
    variabel_navn += 1

print("\n")


# Uendelig løkke:

# while True:
#     print("Pass på")
