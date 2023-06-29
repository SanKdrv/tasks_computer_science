# Дан список строк, необходимо вывести список из списков, которые представляет из себя анаграммы.
# Пример: strs = ["eat","tea","tan","ate","nat","bat"], вывод: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Пример: strs = [""], вывод [[""]]
# Пример: strs = ["a"], вывод [["a"]]

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
sort_words = {}
for word in words:
    sort_words[word] = ''.join(sorted(word))

print(sort_words)
anagrams = []
for i in range(len(words)):
    ana = [words[i]]
    for j in range(i + 1, len(words)):
        if sort_words[words[i]] == sort_words[words[j]]:
            ana.append(words[j])
    if len(ana) != 1:
        anagrams.append(ana)

print(anagrams)