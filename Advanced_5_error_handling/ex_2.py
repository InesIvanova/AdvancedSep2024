text = input()

try:
    num = int(input())
except ValueError:
    print("Variable times must be an integer")
else:
    print(text * num)



