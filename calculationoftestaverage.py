# Program to calculate the best two-test average out of three test marks

# Accepting three test marks from the user
t1 = float(input("Enter Test 1 mark: "))
t2 = float(input("Enter Test 2 mark: "))
t3 = float(input("Enter Test 3 mark: "))

# Put the marks in a list
marks = [t1, t2, t3]

# Sort the list in descending order (highest first)
marks.sort(reverse=True)

# Take the best two marks
best_two_total = marks[0] + marks[1]

# Calculate average
best_two_average = best_two_total / 2

# Display the result
print("Best two-test average:", best_two_average)
