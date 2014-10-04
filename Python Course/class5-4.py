import random as rd
import numpy as np
import pylab as pyplot
from math import sqrt, log, sin , cos, pi


def x(s, t):
    x = sqrt(-2*log(s)*cos(2*pi*t))
    return x


s = rd.random()
t = rd.random()
print(x(s,t))