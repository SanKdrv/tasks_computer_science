# Для заданного массива nums и целого числа k необходимо вывести общее количество подмассивов, сумма чисел в которых равна k.
#
# Пример: nums = [1,1,1], k = 2, вывод: 2, пояснение: [1, 1], [1, 1].
# Пример: nums = [1,2,3], k = 3, вывод: 2, пояснение: [1, 2], [3].
nums = [1, 1, 1]
k = 2


def f(summ, nums):
    res = []
    for i in range(len(nums)):
        summ -= nums[i]
        res.append(nums[i])

        if summ == 0:
            return res

    return False


count = 0
for i in range(len(nums)):
    answer = f(k, nums[i:])
    if answer != False:
        count += 1
        print(answer)

print(count)
