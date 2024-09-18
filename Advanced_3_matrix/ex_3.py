n = int(input())

matrix = []
flat_result = []

for i in range(n):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

matrix = [ [int(el) for el in input().split(", ")] for i in range(n)]

a = [
    [1, 2],
    [3, 4]
]

result_a = []

for row_data in a:
    for el in row_data:
        result_a.append(el)

result_a = [el for row_data in a for el in row_data]

# [1, 2, 3, 4]
    # flat_result.extend(row_data)
    # for el in input().split(", "):
    #     flat_result.append(int(el))


# read matrix as comprehension
# matrix = [[int(el) for el in input().split(", ")] for i in range(n)]

#
# flat_result = []
# for row in matrix:
#     for el in row:
#         flat_result.append(el)
#
#

flat_result = [el for row in matrix for el in row]
print(flat_result)