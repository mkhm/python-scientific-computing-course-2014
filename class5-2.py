import random as rd
import numpy as np
import pylab as pyplot
import math



b=[[1,9],[2,8],[3,7]]

np.savetxt('data.txt',b)

data=np.loadtxt('data.txt')

print(data)
x=data[:,0]
y=data[:,1]

print(x)
print(y)

print(sum(x))

pyplot.plot(x, y)
pyplot.show()