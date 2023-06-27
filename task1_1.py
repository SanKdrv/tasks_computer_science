# Имеется массив целых чисел numbers. Необходимо найти все такие тройки [numbers[i], numbers[j], numbers[k]],
# где i != j, j != k, k != i и сумма numbers[i] + numbers[j] + numbers[k] = 0
# Пример: nums = [4,-1,7,0,1,2,-1,5], тройки: [[-1,-1,2],[-1,0,1]]

nums = [4, -1, 7, 0, 1, 2, -1, 5]
n = len(nums)

for i in range(0, n - 2):
    for j in range(i, n - 1):
        for k in range(j, n):
            if nums[i] + nums[j] + nums[k] == 0:
                if i != j and j != k and k != i:
                    print(nums[i], nums[j], nums[k])
