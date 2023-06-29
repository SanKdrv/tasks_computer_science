# Ограничим правильное использование заглавных букв тремя вариантами: в слове все заглавные (USSR),# в слове все строчные (mother), в слове только первая заглавная (Yandex).
# Дана строка, необходимо вывести True, если использование заглавных букв в нем правильное, False - в противном случае.# Пример: word = "USSR", вывод: True
# Пример: word = "GandR", вывод: False


def isCapitalUsage(word):
    if word.isupper() or word.islower() or word.istitle():
        return True
    else:
        return False

# Примеры использования:
word = "USSR"
print(isCapitalUsage(word))  # True

word = "GandR"
print(isCapitalUsage(word))  # False
