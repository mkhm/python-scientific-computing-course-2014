import random as rd
import numpy as np
import pylab as pyplot
from math import pi,sin


x=np.arange(0,2*pi,pi/100)

y=[sin(n)for n in x]

#pyplot.plot(x,y,label="f(x)",color='yellow')
pyplot.plot(y,x,label="g(x)",color='red')
pyplot.plot(x,y,'og')
#limit=pyplot.axis([0,6,-2,2])
pyplot.xlabel(r"$x$")
pyplot.ylabel(r"$\hbar f(x)(x_{3}^{2}\frac{y}{u})$")

pyplot.legend()

f=np.polyfit(x,y,2)

print(f)
pyplot.show()