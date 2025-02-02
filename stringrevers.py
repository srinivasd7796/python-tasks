def reverse_string(s):
    return s[::-1]

string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))


def reverse_string_using_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

string = input("Enter a string: ")
print("Reversed string:", reverse_string_using_loop(string))


def reverse_string_using_reversed(s):
    return ''.join(reversed(s))

string = input("Enter a string: ")
print("Reversed string:", reverse_string_using_reversed(string))


def reverse_string_using_while(s):
    reversed_str = ""
    index = len(s) - 1
    while index >= 0:
        reversed_str += s[index]
        index -= 1
    return reversed_str

string = input("Enter a string: ")
print("Reversed string:", reverse_string_using_while(string))


def reverse_string_using_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_using_recursion(s[1:]) + s[0]

string = input("Enter a string: ")
print("Reversed string:", reverse_string_using_recursion(string))


from functools import reduce

def reverse_string_using_reduce(s):
    return reduce(lambda x, y: y + x, s)

string = input("Enter a string: ")
print("Reversed string:", reverse_string_using_reduce(string))


def reverse_string_using_stack(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

string = input("Enter a string: ")
print("Reversed string:", reverse_string_using_stack(string))
