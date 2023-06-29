# Дан массив целых чисел, необходимо определить есть ли в нем такая последовательность, что i < j < k и nums[i] < nums[k] < nums[j]
#
# Пример: nums = [1,2,3,4], вывод: False
# Пример: nums = [3,1,4,2], вывод: True, пояснение: [1, 4, 2]
# Пример: nums = [-1,3,2,0], вывод: True, пояснение: имеется три нужных последовательности [-1, 3, 2], [-1, 3, 0] и [-1, 2, 0]

nums = [-1, 3, 2, 0]
for i in range(len(nums)-2):
    for j in range(i, len(nums)-1):
        for k in range(j, len(nums)):
            if i < j < k and nums[i] < nums[k] < nums[j]:
                print(nums[i], nums[j], nums[k])
