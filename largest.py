def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

x, y, z = map(int, input("Enter three numbers: ").split())
print("The largest number is:", largest_of_three(x, y, z))
