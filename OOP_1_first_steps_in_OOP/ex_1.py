def print_row(spaces, stars):
    result = f"{' '* spaces}{'* '*stars}"
    result = result[:-1]
    print(result)


def print_upper_part(n):
    for row in range(1, n + 1):
        spaces = n - row
        print_row(spaces, row)


def print_bottom_part(n):
    for row in range(1, n):
        stars = n - row
        print_row(row, stars)


def print_rhombus(n):
    print_upper_part(n)
    print_bottom_part(n)


n = int(input())
print_rhombus(n)
