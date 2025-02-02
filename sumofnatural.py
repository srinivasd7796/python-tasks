def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

num = int(input("Enter a number: "))
print("Sum of first", num, "natural numbers:", sum_of_natural_numbers(num))
