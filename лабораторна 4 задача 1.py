import math

def func(x):
    return((x + x**2 + x**3 + math.sin(x))**1/3)/(2.27*math.log(math.fabs(x+100), math.e))

    num = int(input("x = "))
    print(func(num))
