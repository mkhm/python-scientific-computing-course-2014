from random import randrange
from pylab import plot, show
from pylab import frange

def f(n):
    s=0
    for i in range(n):
        s+=randrange(2)
    return s

def coin(g, n, N):
    data=[]
    for i in range(N):
        x=g(n)
        data.append(x)
    return data

def distribution(data, dx):
    data_min=min(data)
    data_max=max(data)
    x=[]
    y=[]

    for interval in frange(data_min+dx/2, data_max, dx):
        x.append(interval)
        y.append(0)

    for i in data:
        index=int((i-data_min)/dx)
        y[index]+=1

    return (x, y)


def distribution2(data, m):
    data_min=min(data)
    data_max=max(data)
    dx=(data_max-data_min)/m

    t=distribution(data,dx)
    return t

def distribution3(data, m):
    data_min=min(data)
    data_max=max(data)
    dx=(data_max-data_min)/m
    x=[]
    y=[]

    for interval in frange(data_min+dx/2, data_max, dx):
        x.append(interval)
        y.append(0)

    x.append(data_max+dx/2)
    y.append(0)
    for i in data:
        index=int((i-data_min)/dx)
        y[index]+=1

    return (x, y)



data=coin(f, 100, 100000)
t=distribution3(data,35)
x=t[0]
y=t[1]

plot(x,y)
show()






