from Advanced_8_modules.ex_4.core import execute

expression = input()
num1, sign, num2 = expression.split()
num1 = float(num1)
num2 = float(num2)

print(f"{execute(num1, sign, num2):.2f}")