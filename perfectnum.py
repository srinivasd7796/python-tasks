def is_perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

number = int(input("Enter a number: "))
print(is_perfect_number(number))
