from random import randint


def generate_matrix(N,M):
    matrix = []
    for i in range(N):
        rows = []
        for j in range(M):
            rows.append(randint(0,1))
        matrix.append(rows)
    return matrix


# def find_square(matrix):
#     N = len(matrix)
#     M = len(matrix[0])
#     rank = 0
#     max = 0
#     for i in range(N):
#         for j in range(M):
#             if matrix[i][j] == 1:
#                 rank = 1
#                 a = i
#                 b = j
#                 while matrix[i][a] == 1:
#                     while matrix[b][j] == 1:
#                         while
#                 if rank >= max:
#                     max = rank


def max_square(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0] * m for _ in range(n)]
    max_size = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                max_size = max(max_size, dp[i][j])
    return max_size


body = generate_matrix(5, 5)
for i in range(len(body)):
    print(body[i])
print(max_square(body))

# while True:
#     newbody = generate_matrix(5,5)
#     if max_square(newbody) == 3:
#         for i in range(len(newbody)):
#             print(newbody[i])
#         break