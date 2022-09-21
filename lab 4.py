import math
x = float(input("x = "))
def f(x):
    ((x + x**2 + x**3 + math.sin(x))**1/3)/(2.27*math.log(math.fabs(x+100), math.e))
print(f"(x)", f)