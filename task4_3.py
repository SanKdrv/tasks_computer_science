# Дана доска m x n, с буками и исходное слово. Необходимо определенить можно ли на доске найти исходное слово.
# Слово конструируется из соседних ячеек по горизонтали или вертикали.
#  Пример: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED", вывод: true
#  Пример: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE", вывод: true
#  Пример: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB", вывод: false


def exist(board, word):
    if not board:
        return False

    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            if dfs(board, i, j, word):
                return True

    return False

def dfs(board, i, j, word):
    if len(word) == 0:
        return True

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
        return False

    temp = board[i][j]
    board[i][j] = "#"

    result = dfs(board, i + 1, j, word[1:]) or \
             dfs(board, i - 1, j, word[1:]) or \
             dfs(board, i, j + 1, word[1:]) or \
             dfs(board, i, j - 1, word[1:])

    board[i][j] = temp

    return result

# Примеры использования:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))  # True

word = "SEE"
print(exist(board, word))  # True

word = "ABCB"
print(exist(board, word))  # False


