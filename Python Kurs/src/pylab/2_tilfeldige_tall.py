import pylab

tilfeldige_tall = pylab.zeros(20)
for i in range(len(tilfeldige_tall)):
    tilfeldige_tall[i] = pylab.randint(1, 10)

# 20 tilfeldige heltall mellom 1 og 9
print(tilfeldige_tall)

for i in range(len(tilfeldige_tall)):
    tilfeldige_tall[i] = pylab.uniform(0, 1)

# 20 tilfeldige desimaltall mellom 0 og 1
print(tilfeldige_tall)
