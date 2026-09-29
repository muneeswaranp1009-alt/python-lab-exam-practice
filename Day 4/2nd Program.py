#2. Write a python program to find the product of two matrices

x = [[1,3,4],
    [5,7,3],
    [6,7,8]]

y = [[3,6,7],
    [4,6,8],
    [4,9,5]]

r = [[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            r[i][j] += x[i][k] *y[k][j]
for result in r:
    print(result)