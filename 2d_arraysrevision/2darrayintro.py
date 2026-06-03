#going to revise arrays and stuff to enhance learning and all
#2d array
matrix = [1,2,3,
          4,5,6,
          7,8,9]

#for accessing an element in the 2d array
#the way is like matrix[row][column]

matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in range(len(matrix2)):

    for col in range(len(matrix2[0])):

        print(matrix2[row][col], end=" ")

    print()


target = 5
#now implementing the linear search
for row in range(len(matrix2)):
    for col in range(len(matrix2[0])):

        if matrix2[row][col] == target:
            print(row, col)

#now implementing the linear search
