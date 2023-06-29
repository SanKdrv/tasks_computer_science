# Дан массив из целых чисел. Необходимо найти максимальную сумму подряд стоящих элементов.
# Пример: [-2,1,-3,4,-1,2,1,-5,4], вывод: 6, пояснение: [4, -1, 2, 1]
# Пример: [1], вывод: 1, пояснение: [1]
# Пример: [5,4,-1,7,8], вывод: 23, пояснение: [5,4,-1,7,8]

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = 0
for i in range(len(array)):
    sum = 0
    for j in range(i, len(array)):
        sum += array[j]
        max_sum = max(sum, max_sum)
print(max_sum)