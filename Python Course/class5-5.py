
x=1
a=100
b=1875765
c=78575

for i in range(10):
    x=(a*x+b) % c
    print(x/c)
