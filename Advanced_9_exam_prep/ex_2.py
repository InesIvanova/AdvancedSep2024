def calculate_next_point(direction, direction_mapper, current_row_index, current_col_index, n):
    # Without mapper
    # if direction == "down":
    #     current_row_index += 1
    # elif direction == "up":
    #     current_row_index -= 1
    # elif direction == "left":
    #     current_col_index -= 1
    # else:
    #     current_col_index += 1
    # next_row_index = current_row_index % n
    # next_col_index = current_col_index % n

    # With mapper
    next_row_index = current_row_index + direction_mapper[direction][0]
    next_col_index = current_col_index + direction_mapper[direction][1]

    next_row_index = next_row_index % n
    next_col_index = next_col_index % n

    return next_row_index, next_col_index


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

n = int(input())

matrix = []
bee_position = None
bee_energy = 15
nectar = 0
restored_energy = False

for row_index in range(n):
    row_data = list(input())
    if "B" in row_data:
        col_index = row_data.index("B")
        bee_position = (row_index, col_index)
    matrix.append(row_data)


while True:
    direction = input()

    current_row_index, current_col_index = bee_position
    next_row_index, next_col_index = calculate_next_point(direction, direction_mapper, current_row_index, current_col_index, n)

    element = matrix[next_row_index][next_col_index]
    matrix[current_row_index][current_col_index] = "-"
    matrix[next_row_index][next_col_index] = "B"
    bee_position = (next_row_index, next_col_index)
    bee_energy -= 1

    if element.isdigit():
        nectar += int(element)

    elif element == "H":
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
        else:
            print(f"Beesy did not manage to collect enough nectar.")
        break

    if bee_energy <= 0 and nectar < 30:
        print(f"This is the end! Beesy ran out of energy.")
        break

    if bee_energy <= 0 and nectar >= 30 and not restored_energy:
        diff = nectar - 30
        bee_energy += diff
        nectar = 30
        restored_energy = True

    if bee_energy <= 0:
        print(f"This is the end! Beesy ran out of energy.")
        break


for row in matrix:
    print(*row, sep="")
