matrix = [[1,2,3],
          [0,9,8],
          [4,5,6]]

transposed=[[0]*3 for _ in range(3)]

for i in range(3):
    for j in range (3):
        transposed[i][j] = matrix[j][i]

print(transposed)

transp=[[matrix[n][m] for n in range(3)]for m in range(3)]
print(transp)