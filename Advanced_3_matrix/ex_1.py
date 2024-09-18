row_count, col_count = [int(el) for el in input().split(", ")]

matrix = []
elements_sum = 0


for row in range(row_count):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)
    elements_sum += sum(row_data)


print(elements_sum)
print(matrix)

print(sum([1, 2]))