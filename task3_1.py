# В списке из строк найти максимальный общий префикс.
# Пример: strs = ["flower","flow","flight"], вывод: "fl"
# Пример: strs = ["dog","racecar","car"], вывод: ""
# Считать, что в строках могут использоваться только латинские буквы.

def longestCommonPrefix(my_str):
    if my_str == []:
        return ''
    if len(my_str) == 1:
        return my_str[0]
    my_str.sort()
    shortest = my_str[0]
    prefix = ''
    for i in range(len(shortest)):
        if my_str[len(my_str) - 1][i] == shortest[i]:
            prefix += my_str[len(my_str) - 1][i]
        else:
            break
    return prefix


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))