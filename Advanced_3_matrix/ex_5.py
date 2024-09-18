n = int(input())

matrix = []

for i in range(n):
    row_data = [int(el) for el in input().split(" ")]
    matrix.append(row_data)


diagonal_sum = 0
for index in range(n):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)