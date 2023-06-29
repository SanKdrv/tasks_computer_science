# Для заданного целого положительного числа c определить существуют ли такие числа a и b, что a * a + b * b = c.
#
# Пример: c = 5, вывод: True, пояснение: 1 * 1 + 2 * 2 = 5
# Пример: c = 3, вывод: False

def check_sum_of_squares(c):
    for a in range(1, c):
        for b in range(1, c):
            if a * a + b * b == c:
                return True
    return False

# Примеры использования:
c = 5
print(check_sum_of_squares(c))  # True

c = 3
print(check_sum_of_squares(c))  # False