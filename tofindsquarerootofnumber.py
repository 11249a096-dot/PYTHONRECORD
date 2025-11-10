# AIM:
# To find the square of numbers using Python.

# ALGORITHM:
# 1. Start the program.
# 2. Take a number as input from the user.
# 3. Calculate its square using the exponent operator (**).
# 4. Display the result.
# 5. End the program.

# PROGRAM:
# Step 1: Take input from the user
num = int(input("Enter a number: "))
# Step 2: Calculate the square of the number
square = num ** 2
# Step 3: Display the result
print("The square of", num, "is", square)

import math

# Input from the user
num = float(input("Enter a number: "))

# Check if the number is non-negative
if num >= 0:
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt}")
else:
    print("Cannot compute the square root of a negative number.")
