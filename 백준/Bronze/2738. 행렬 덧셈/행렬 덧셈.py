n, m = map(int, input().split())

matrix1 = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(n, n*2)]

for i in range(n):
    for j in range(m):
        print(matrix1[i][j]+matrix2[i][j], end=' ')
    print()