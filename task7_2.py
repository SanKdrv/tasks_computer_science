# Даны две строки s1 и s2. Необходимо вернуть True, если хотя бы одна из перестановок s1 содержится в s2.
# Строки могут содержать только латинские строчные буквы.
# Пример: s1 = "ab", s2 = "eidbaooo", вывод: True
# Пример: s1 = "aooob", s2 = "eidboaoo", вывод: True
# Пример: s1 = "ab", s2 = "eidboaoo", вывод: False


s1 = "aooob"
s2 = "eidboaoo"

s1 = sorted(s1)
flag = False

for i in range(len(s2)-len(s1)+1):
    string = s2[i:i+len(s1)]
    if s1 == sorted(string):
        flag = True
        break

print(flag)
