# Funksjoner lages med kodeordet def for definition:
def x_plus_y(x, y):
    return x + y


# Merk at print også er en funksjon under bruker vi funksjonen x_plus_y på tallene 5 og 7,
# og resultatet av x_plusy funksjonen sendes inn til print funksjonen
print(x_plus_y(5, 7))

# Math er et bibliotek, jeg bruker det i sjekk_for_primtall funksjonen
import math


def sjekk_for_primtall(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            # return hopper ut av funksjonen med en gang, resten av for løkka kjøres ikke
            return False
    return True


primtall = []
for i in range(100):
    if sjekk_for_primtall(i):
        primtall.append(i)

print(primtall)
