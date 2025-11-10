// AIM:To find a value using Linear Search in Python.

//ALGORITHM:
//1. Start the program.
//2. Define a list of elements.
//3. Take the element to be searched (key) as input from the user.
//4. Traverse the list using a loop.
//5. Compare each element of the list with the key.
//6. If a match is found, display the position and stop the search.
//7. If the loop ends without finding the key, display "Element not found".
//8. End the program.

# PROGRAM:

numbers = [10, 25, 30, 45, 50, 65, 70]
key = int(input("Enter the value to search: "))
found = False
for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at position", i + 1)
        found = True
        break
