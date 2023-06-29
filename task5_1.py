# Дана строка s и массив строк wordDict. Необходимо вернуть True, если слово s можно
# составить из слов в массиве wordDict. Слово из workDict может быть использовано в s любое количество раз.
# Пример: s = "applepenapple", wordDict = ["apple","pen"], вывод: True
# Пример: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"], вывод: False


def wordBreak(s, wordDict):
    if not s:
        return True

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[n]


# Примеры использования:
s = "applepenapple"
wordDict = ["apple", "pen"]
print(wordBreak(s, wordDict))  # True

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))  # False
