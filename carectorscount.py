def count_occurrences(s, char):
    return s.count(char)

string = input("Enter a string: ")
character = input("Enter the character to count: ")
print(f"The character '{character}' appears {count_occurrences(string, character)} times.")
