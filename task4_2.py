# Дана строка из цифр. Необходимо восстановить из нее все возможные корректные IP адреса.
# Нельзя удалять в строке или изменять порядк цифр в ней.
# Пример: "25525511135", вывод: ["255.255.11.135","255.255.111.35"]
# Пример: "0000", вывод: ["0.0.0.0"]
# Пример: "101023", вывод: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


def restore_ip_addresses(s):
    result = []
    dfs(s, 0, '', result)
    return result


def dfs(s, index, path, result):
    if index == 4:
        if s == '':
            result.append(path[:-1])  # Удаляем последнюю точку
        return
    for i in range(1, 4):
        if i <= len(s):
            if i == 1:
                dfs(s[i:], index + 1, path + s[:i] + '.', result)
            elif i == 2 and s[0] != '0':
                dfs(s[i:], index + 1, path + s[:i] + '.', result)
            elif i == 3 and s[0] != '0' and int(s[:3]) <= 255:
                dfs(s[i:], index + 1, path + s[:i] + '.', result)


# Примеры использования:
s = "25525511135"
print(restore_ip_addresses(s))  # ["255.255.11.135","255.255.111.35"]

s = "0000"
print(restore_ip_addresses(s))  # ["0.0.0.0"]

s = "101023"
print(restore_ip_addresses(s))  # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3"]
