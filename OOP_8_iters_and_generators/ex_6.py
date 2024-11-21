def something():

    yield 1


result = something()
print(result)
for el in result:
    print(el)
