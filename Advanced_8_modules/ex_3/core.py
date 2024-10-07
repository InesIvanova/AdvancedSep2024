def print_upper_part(n, row=1):
    # Example with recursion
    if row > n:
        return
    for num in range(1, row+1):
        print(num, end=" ")
    print()
    print_upper_part(n, row+1)


def print_bottom_part(n):
    # Example without recursion
    for row in range(1, n):
        end_num = n - row
        for num in range(1, end_num+1):
            print(num, end=" ")
        print()


def print_triangle(n):
    print_upper_part(n)
    print_bottom_part(n)


print_upper_part(3)