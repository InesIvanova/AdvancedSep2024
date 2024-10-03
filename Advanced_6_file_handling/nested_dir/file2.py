file = open("nested.txt", "w")
print(file.closed)
rows = ["row1\n", "row2\n"]

file.writelines(rows)
file.close()
print(file.closed)

with open("nested.txt", "w") as file:
    print(file.closed)
