# Даны два положительных целых числа в виде строк.
# Необходимо выполнить их умножения без преобразования к целому числу (нельзя использовать функцию int).
# Пример: num1 = "2", num2 = "3", вывод: "6"
# Пример: num1 = "123", num2 = "456", вывод: "56088"


num1 = "123"
num2 = "456"
res1 = 0
res2 = 0
# Без int
for i in range(len(num1)):
    res1 += (ord(num1[i])-48) * 10**(len(num1)-i-1)
for i in range(len(num2)):
    res2 += (ord(num2[i])-48) * 10**(len(num2)-i-1)
print(res1*res2)
print(int(num1)*int(num2))
