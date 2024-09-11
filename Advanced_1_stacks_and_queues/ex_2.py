expression = input()

stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        most_recent_parentheses_index = stack.pop()
        print(expression[most_recent_parentheses_index:index+1])