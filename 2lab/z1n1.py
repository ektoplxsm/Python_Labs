# z1n1
a = int(input())
b = int(input())
if a > b:
    print(b)
if b > a:
    print(a)


# мой вариант решения
x = [2, 3]
ln = x[0] if x else None
for i in x:
    if i < ln:
        ln = i
print("Smallest element is :", ln)