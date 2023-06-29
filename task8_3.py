# Дан массив pairs из n пар, где pairs[i] = [left, right], и left < right.
# Пара p2 = [c, d] следует за парой p1 = [a, b], если b < c.
# Необходимо вернуть длину максимальной последовательность из пар, которые можно составить из pairs.
# Пример: pairs = [[1,2],[2,3],[3,4]], вывод: 2, пояснение [1,2] -> [3,4]
# Пример: pairs = [[1,2],[7,8],[4,5]], вывод: 3, пояснение [1,2] -> [4,5] -> [7,8]


def findMaxLength(pairs):
    pairs.sort(key=lambda x: x[1])  # Сортируем массив pairs по возрастанию значений правых элементов пар

    n = len(pairs)
    dp = [1] * n  # Инициализируем массив dp значением 1, так как каждая пара сама по себе является последовательностью длины 1

    for i in range(n):
        for j in range(i):
            if pairs[j][1] < pairs[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Возвращаем максимальное значение из массива dp


# Примеры использования:
pairs = [[1, 2], [2, 3], [3, 4]]
print(findMaxLength(pairs))  # 2

pairs = [[1, 2], [7, 8], [4, 5]]
print(findMaxLength(pairs))  # 3
