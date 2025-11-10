// AIM:To find the square of numbers using Python.

//ALGORITHM:
//1. Start the program.
//2. Take a number as input from the user.
//3. Calculate its square using the exponent operator (**).
//4. Display the result.
//5. End the program.

//PROGRAM:
num = int(input("Enter a number: "))
square = num ** 2
print("The square of", num, "is", square)

import math

num = float(input("Enter a number: "))
if num >= 0:
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt}")
else:
    print("Cannot compute the square root of a negative number.")
