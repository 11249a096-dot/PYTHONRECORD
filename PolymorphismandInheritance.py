# -------------------------------
# Base Class
# -------------------------------
class PalindromeChecker:
    def __init__(self, value):
        self.value = value

    def is_palindrome(self):
        return False     # To be overridden


# -------------------------------
# Derived Class for String
# -------------------------------
class StringPalindrome(PalindromeChecker):
    def is_palindrome(self):
        s = self.value.lower()            # Normalize
        return s == s[::-1]


# -------------------------------
# Derived Class for Integer
# -------------------------------
class IntegerPalindrome(PalindromeChecker):
    def is_palindrome(self):
        num_str = str(self.value)         # Convert to string
        return num_str == num_str[::-1]


# -------------------------------
# Main Program
# -------------------------------
print("Palindrome Check using Inheritance & Polymorphism")

user_input = input("Enter a value (string or integer): ")

# Check if input is an integer
if user_input.isdigit():
    obj = IntegerPalindrome(int(user_input))
else:
    obj = StringPalindrome(user_input)

# Polymorphic call
if obj.is_palindrome():
    print(f"'{user_input}' is a Palindrome.")
else:
    print(f"'{user_input}' is NOT a Palindrome.")
