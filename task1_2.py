# Имеется массив целых чисел numbers. Необходимо найти все последовательности в массиве (подряд стоящие числа),
# сумма которых равна заданному числу S.
# Пример: nums = [4,-1,7,0,1,2,-1,5], S = 3, последовательности: [4, -1], [0, 1, 2], [1, 2]

nums = [4, -1, 7, 0, 1, 2, -1, 5]
S = 3
answer = []
n = len(nums)
for i in range(0, n):
    array = []2
    Summ = 0
    j = i
    while j != n:
        Summ += nums[j]
        array.append(nums[j])
        if Summ > S:
            break
        if Summ == S:
            answer.append(array)
            break
        j += 1
print(answer)