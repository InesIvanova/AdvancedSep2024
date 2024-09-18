# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
#
#
# for row_data in matrix:
#     for el in row_data:
#         print(el)
#
#

a = [1, 2]
print(a)
a[0] = 100
print(a)

# b = [3, 4]

# for el in b:
#     a.append(el)
# a.extend(b)
# print(a)

# matrix = [
#     [1, 2],
#     [3, 4]
# ]
#
# matrix[1][0] = 100
# print(matrix)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        matrix[row_index][col_index] += 1



print(matrix)
# [[2, 3, 4], [5, 6, 7], [8, 9 ,10]]



