import math
a = float(input("a = "))
b = float(input("b = "))
t = float(input("t = "))

R = 8.81*t*a + math.asin(math.cos(a+b))+math.sqrt(t+b)

print(R)
