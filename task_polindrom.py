a = [-1, -3, 10, 20, 21, 4, 3, 22, 10, -2, 15]

a.sort()

max_dif = 0

for el in range(len(a) - 1):
    x = abs(a[el]) - abs(a[el + 1])
    if abs(x) > max_dif:
        max_dif = abs(x)


print(max_dif)
