# NOTE: Pylab er et bibliotek som kombinerer numpy og matplotlib,
# man bør egentlig bruke disse hver for seg for å holde tunga rett i munnen,
# men elevene blir lært oppt il å bruke pylab, så det er det vi bruker her også

# Pylab har ikke like mye funksjonalitet som matplotlib, men er nok lettere å lære seg

# Hvis man velger å bruke matplotlib istedenfor pylab, må man skrive ting på en litt annen måte

# Kunne brukt "import numpy"
import pylab


# OBS OBS: Pass på å vite om du jobber med en liste eller array, de oppfører seg forskjellig
vanlig_liste = [1, 2, 3, 4, 5]
numpy_array = pylab.array(vanlig_liste)
print("Typen til vanlig_liste:", type(vanlig_liste))
print("Typen til numpy_array:", type(numpy_array))

# Man kan gjøre matematiske operatorer på en numpy array og et vanlig tall
print(vanlig_liste)
print(vanlig_liste * 2)  # Gjør lista dobbelt så lang
print()
print(numpy_array)
print(numpy_array * 2)  # Gang hvert element med 2
print(numpy_array - 3)  # Trekk 3 fra hvert element
print(numpy_array**2)  # Opphøy hvert element i andre

# Tenk på numpy arrays som en vektor, ALT du kan gjøre med en vektor kan du gjøre med en numpy array
# Bare søk opp funksjonalitet hvis du lurer på hvordan du gjør ting

print("\nZeroes:\n")

# Numpy har også funksjonalitet for å lage arrays på en lett måte

numpy_array_med_nuller = pylab.zeros(20)
# Lager en liste med 20 nuller (av type decimaltall)
print(numpy_array_med_nuller)
print(type(numpy_array_med_nuller[0]))

print("\nLinspace:\n")

numpy_array_mellom_1_og_10 = pylab.linspace(1, 10, 91)
# Lager en liste med tall mellom 1 og 10, med 91 elementer i lista
print(numpy_array_mellom_1_og_10)
print(type(numpy_array_mellom_1_og_10[0]))
