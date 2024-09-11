from collections import deque

available_liters = int(input())

name = input()
customers = deque()

while name != "Start":
    customers.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        customer = customers.popleft()
        liters_wanted = int(command)
        if liters_wanted <= available_liters:
            available_liters -= liters_wanted
            print(f"{customer} got water")
        else:
            print(f"{customer} must wait" )
    else:
        refill_command, liters = command.split()
        liters = int(liters)
        available_liters += liters
    command = input()

print(f"{available_liters} liters left")