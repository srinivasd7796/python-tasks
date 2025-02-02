def is_armstrong(num):
    num_str = str(num)
    order = len(num_str)
    sum_of_powers = sum(int(digit) ** order for digit in num_str)
    return sum_of_powers == num

number = int(input("Enter a number: "))
print(is_armstrong(number))
