import pylab

x = [-3, -2, -1, 0, 1, 2, 3]
# x = pylab.array([-3, -2, -1, 0, 1, 2, 3])
# x = pylab.linspace(-3, 3, 7)

y = [9, 4, 1, 0, 1, 4, 9]
# y = x**2

pylab.plot(x, y)
pylab.show()
