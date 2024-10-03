from math import ceil


def print_board(board):
    for row in board:
        print(f"|  {'  |  '.join([str(el) for el in row])}  |")


player_one_name = input("Player one name: ")
player_two_name = input("Player two name: ")
while True:
    sign = input(f"{player_one_name} would you like to play with X or O? ").upper()
    if sign in ("X", "O"):
        break


other_player_sign = "O" if sign == "X" else "X"
player_one = (player_one_name, sign)
player_two = (player_two_name, other_player_sign)

num_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_board(num_board)


board = [[" ", " ", " "] for _ in range(3)]
print(f"{player_one[0]} starts first!")
turns = 1
current_player = None
result = None

while True:
    current_player = player_one if turns % 2 != 0 else player_two
    position = input(f"{current_player[0]} choose a free position [1-9]: ")

    try:
        position = int(position)
    except ValueError:
        print("Position must be valid number between 1 and 9 (inclusive).")
        continue

    if position < 1 or position > 9:
        print("Position must be valid number between 1 and 9 (inclusive).")
        continue

    selected_row_index = ceil(position / 3) - 1
    selected_col_index = position % 3 - 1
    if board[selected_row_index][selected_col_index] != " ":
        print("You must select an empty position!")
        continue

    board[selected_row_index][selected_col_index] = current_player[1]
    print_board(board)
    turns += 1

    if turns >= 6:
        first_row = all([el == current_player[1] for el in board[0]])
        second_row = all([el == current_player[1] for el in board[1]])
        third_row = all([el == current_player[1] for el in board[2]])

        first_column = all(
            [
                el == current_player[1]
                for el in [board[0][0], board[1][0], board[2][0]]
            ]
        )
        second_column = all(
            [
                el == current_player[1]
                for el in [board[0][1], board[1][1], board[2][1]]
            ]
        )
        third_column = all(
            [
                el == current_player[1]
                for el in [board[0][2], board[1][2], board[2][2]]
             ]
        )

        first_diagonal = all(
            [
                el == current_player[1]
                for el in [board[0][0], board[1][1], board[2][2]]
            ]
        )
        second_diagonal = all(
            [
                el == current_player[1]
                for el in [board[0][2], board[1][1], board[2][0]]
            ]
        )

        if any(
            [
                first_row,
                second_row,
                third_row,
                first_column,
                second_column,
                third_column,
                first_diagonal,
                second_diagonal,
            ]
        ):

            result = f"{current_player[0]} won!"
            break

        if turns == 9:
            result = "DRAW! No one wins!"
            break

print(result)

with open("game_results.txt", "a") as file:
    file.write(result + "\n")