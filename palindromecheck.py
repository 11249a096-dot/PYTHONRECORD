# Program to check palindrome and count digit occurrences

# Input from user
num = input("Enter a number: ")

# Palindrome check
if num == num[::-1]:
    print("It is a Palindrome.")
else:
    print("It is NOT a Palindrome.")

# Digit occurrence count
print("\nDigit Occurrences:")
for digit in range(10):
    count = num.count(str(digit))
    if count > 0:
        print(f"Digit {digit}: {count} time(s)")
