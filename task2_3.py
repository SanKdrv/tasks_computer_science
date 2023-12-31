# Для заданного числа n, вывести n-ое число, простыми делителями которого являются числа из 1, 2, 3 и 5.
# Пример: n = 10, вывод: 12 (первые десять чисел удовлетворяющих условию: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12])
# Пример: n = 1, вывод: 1


def delit(num):
    # Делим на 5 пока нет остатка
    while num % 5 == 0:
        num //= 5
    # Делим на 3 пока нет остатка
    while num % 3 == 0:
        num //= 3
    # Делим на 2 пока нет остатка
    while num % 2 == 0:
        num //= 2
    return num


n = int(input())
count = 0
i = 1

while count < n:
    res = delit(i)
    if res == 1:
        count += 1
        print(i)
    i += 1


