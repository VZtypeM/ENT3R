liste = ["Python", "er", "nice"]
print("Typen til lista er:", type(liste))
print("Innholdet i lista er:", liste)
print("Lengden av lista er", len(liste))
print("Første elementet i lista er:", liste[0])

# Lister er indexert, slik at de starter på 0 og øker med 1,
# i python er det faktisk slik at index -1 betyr siste element, og -2 betyr nest siste, osv

print("Nest siste element i lista er:", liste[-2])
print("Andre element i lista er:", liste[1])

print()

tall = [3, 5, 4, 8, 6, 1, 9]

tall.sort()
print(tall)

tall.insert(2, 7)  # Sett inn 7 på index 2
print(tall)
