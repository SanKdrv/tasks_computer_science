# Теорема Лагранжа о сумме четырёх квадратов"
# Формулировка: всякое натуральное число можно представить в виде суммы ЧЕТЫРЕХ квадратов целых чисел


n = int(input())
sqrt = int(n**(1/2)) + 1
res = []


for i in range(0, sqrt):
    for j in range(0, sqrt):
        for k in range(0, sqrt):
            for m in range(0, sqrt):
                if i**2 + j**2 + k**2 + m**2 == n:
                    if i != 0:
                        res.append(i)
                    if j != 0:
                        res.append(j)
                    if k != 0:
                        res.append(k)
                    if m != 0:
                        res.append(m)
                    print(res)
                    exit(0)


print(-1)
