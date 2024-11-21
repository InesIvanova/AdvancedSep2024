def squares(n):
    num = 1
    while num <= n:
        yield num * num
        num += 1


result = squares(5)
result_list = []
for el in result:
    result_list.append(el)
print(result_list)