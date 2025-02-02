def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()  # Clean the input string
    return s == s[::-1]

string = input("Enter a string: ")
print(is_palindrome(string))
