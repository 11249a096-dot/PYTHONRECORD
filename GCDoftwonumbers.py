// AIM:To compute the Greatest Common Divisor (GCD) of two integers using Python.

// ALGORITHM:
//1. Import the math module which contains the gcd function.
//2. Take two integer inputs from the user. 
//3. Use math.gcd(a, b) to compute the GCD.
//4. Display the result.
import math  # Step 1: Importing the math module
//Step 2: Taking input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
//Step 3: Calculating the GCD using built-in function
gcd = math.gcd(a, b)
//Step 4: Displaying the result
print(f"The GCD of {a} and {b} is {gcd}")

import math
//Define two numbers
a = 36
b = 60

# Compute GCD
gcd = math.gcd(a, b) 

print(f"The GCD of {a} and {b} is {gcd}")
