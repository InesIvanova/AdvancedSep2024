row_count = int(input())

matrix = []

for i in range(row_count):
    row_data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(row_data)

print(matrix)

# even_matrix = []
#
# for row_index in range(len(matrix)):
#     even_matrix.append([])
#     for col_index in range(len(matrix[row_index])):
#         if matrix[row_index][col_index] % 2 == 0:
#             even_matrix[row_index].append(matrix[row_index][col_index])
#
#
# print(even_matrix)

# with comprehension
# print([[el for el in row if el % 2 == 0] for row in matrix])