# Дано целое число и список из целых чисел. Необходимо вывести число комбинаций, которыми можно разложить заданное число числами из заданного списка. Число из списка может использоваться неограниченное количество раз.
# Пример: amount = 5, nums = [1,2,5], вывод: 4, пояснение: 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1
# Пример: amount = 3, nums = [2], вывод: 0
# Пример: amount = 10, nums = [10], вывод: 1

def search_sum(amount, res=[]):
    global s
    for n in nums:
        p = amount - n
        if p == 0:
            res.append(str(n))
            s.add("+".join(sorted(res)))
        elif p > 0:
            search_sum(p, res+[str(n)])
amount = 23
nums = [3,5,4,13]
s = set()
search_sum(amount)
if len(s) == 0:
    s.add('0')
print(len(s))
