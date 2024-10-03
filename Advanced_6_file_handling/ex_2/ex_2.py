# file = open("numbers.txt")
#
# content = file.read().split("\n")
#
# total_sum = 0
#
# for el in content:
#     try:
#         total_sum += int(el)
#     except ValueError:
#         continue
#
# print(total_sum)


file = open("numbers.txt")

content = file.readlines()

total_sum = 0

for el in content:
    total_sum += int(el[:-1])

print(total_sum)