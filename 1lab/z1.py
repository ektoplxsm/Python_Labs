import math
from math import sin, cos

x = int(input("Введите число :"))
y = 1 - (1 / 4 * 2 ** sin((2 * x))) + cos(4 * x)
print(y)

a = int(input("Введите число :"))
b = int(input("Введите число :"))
N = int(input("Введите число :"))
Y = int(input("Введите число :"))
print(2 * Y + (2 * N - 1) * a + 2 * (N - 1) * b)
