# AIM: 
# To compute the exponential value of a number using Python programming.

# ALGORITHM:
# 1. Import the math module which provides the exp() function.
# 2. Take a number as input from the user.
# 3. Use math.exp(x) to calculate e raised to the power of x (i.e., e^x).
# 4. Display the result.

import math

x = float(input("Enter the exponent value (x): "))
result = math.exp(x)
print(f"The exponential of {x} (i.e., e^{x}) is {result}") 
