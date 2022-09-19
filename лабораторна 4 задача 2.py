import math

def func(x):
    return ((x + x**2 + x**3 + math.sin(x))**1/3)/(2.27*math.log(math.fabs(x+1)))

    num = int(input("x = "))
    print(func(num))


    # ------------ 2

    a = float(input("a = "))
    b = float(input("b = "))
    t = float(input("t = "))

    R = 8.81*t*a + math.asin(math.cos(a+b))+math.sqrt(t+b)