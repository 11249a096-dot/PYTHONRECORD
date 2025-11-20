def display_first_n_lines(filename, n):
    try:
        with open(filename, "r") as file:
            print(f"\nFirst {n} lines of the file:")
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line, end="")
    except FileNotFoundError:
        print("Error: File not found!")

def word_frequency(filename, word):
    try:
        with open(filename, "r") as file:
            text = file.read().lower()
            word = word.lower()
            count = text.split().count(word)
            print(f"\nFrequency of '{word}' in the file: {count}")
    except FileNotFoundError:
        print("Error: File not found!")


# --------------------------
# Main Program
# --------------------------
filename = input("Enter the file name: ")
n = int(input("Enter number of lines to display: "))
word = input("Enter the word to find frequency: ")

display_first_n_lines(filename, n)
word_frequency(filename, word)
