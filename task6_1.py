# Преобразовать целое число в десятичной системе счисления в семяричную и вывести ввиде строки.
# Пример: num = 100, вывод: "202"
# Пример: num = -7, вывод: "-10"

num = 7
string = ''
flag = False
if num < 0:
    flag = True
    num = num * (-1)
while num != 0:
    string += str(num % 7)
    num = num // 7
if flag == True:
    string = '-' + string[::-1]
else:
    string = string[::-1]
print(string)