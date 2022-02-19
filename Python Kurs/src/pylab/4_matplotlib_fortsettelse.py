import pylab


def f(x):
    return x**2 - 2 * x + 3


def g(x):
    return 10 * pylab.sin(x + 5) + 20


def h(x):
    # exp er e**x funksjonen
    return pylab.exp(x) + 5


x = pylab.linspace(-10, 10, 100)

# Kan ha flere funksjoner i samme vindu
pylab.plot(x, f(x), color="blue", label="f")
pylab.plot(x, g(x), color="green", label="g")

# Og de kan være på ulike deler av x-aksen
x = pylab.linspace(-5, 5, 100)

pylab.plot(x, h(x), color="red", label="h")


# Alt etter denne kommentaren er styling:
pylab.xlabel("x")  # aksetittel langs x-aksen
pylab.ylabel("y")  # aksetittel langs y-aksen

pylab.axhline(y=0, color="black")  # legger til en vannrett linje (x-akse)
pylab.axvline(x=0, color="black")  # legger til en loddrett linje (y-akse)

pylab.grid()  # legger til et rutenett

pylab.xlim(-11, 11)  # begrenser x-verdiene vi vil vise
pylab.ylim(-10, 160)  # begrenser y-verdiene vi vil vise

pylab.legend()  # Viser label på grafene

pylab.show()
