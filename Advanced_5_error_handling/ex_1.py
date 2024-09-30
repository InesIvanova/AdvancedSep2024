numbers_list = [int(el) for el in input().split(", ")]
result = 1

for el in numbers_list:
    if el <= 5:
        result *= el
    elif 5 < el <= 10:
        result /= el

print(result)
