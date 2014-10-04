


def f():
    y=[]
    x = [i for i in range(-5,5)]
    for i in range(10):
        y.append(i**2)

    tup=(x,y)

    return tup



t=f()

print(t[0][1])
print(t[0])
print(t[1])
