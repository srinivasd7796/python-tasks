def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print(" * " * (2 * i - 1))
rows = int(input("Enter the number of rows: "))
print_star_pattern(rows)


def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print(" * " * (2 * i))
rows = int(input("Enter the number of rows: "))
print_star_pattern(rows)
