def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))
