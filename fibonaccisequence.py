# Function to print Fibonacci sequence up to N terms
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Main program
N = int(input("Enter the value of N (N > 0): "))

# Input validation
if N <= 0:
    print("Error: N must be greater than 0.")
else:
    fibonacci(N)
