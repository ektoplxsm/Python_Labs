x = int(input(" x = "))
a = int(input(" a = "))
b = int(input(" b = "))
c = int(input(" c = "))


def f(x, a, b, c):
    if (c < 0) and (x != 0):
        return (-a * x) - c
    elif (c > 0) and (x == 0):
        return (x - a) / -c
    else:
        return (b * x) / (c -a)


print(f(x, a, b, c))
