def print_star_pattern(rows: int):
    for i in range(1, rows + 1):
        print("   " * (rows - i), end=" ")
        print(" * " * (2 * i - 1))
print_star_pattern(9)
