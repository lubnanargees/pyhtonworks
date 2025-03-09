# Exercise 1: Read and display a file's contents

file1=open("C:\\Users\\User\\Desktop\\sample.txt",'r')
print(file1.read())

file2=open("C:\\Users\\User\\Desktop\\sample2.txt",'w')
file2.close()

# Exercise 2: Copy contents of one file to another
def copy_file(source, destination):
    try:
        with open(source, "r") as src, open(destination, "w") as dest:
            dest.write(src.read())
        print("File copied successfully.")
    except FileNotFoundError:
        print("Error: Source file not found.")

Example usage
copy_file("sample.txt", "sample2.txt")

# Exercise 3: Count the total number of words in a file
def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            print("Total words:", len(words))
    except FileNotFoundError:
        print("Error: File not found.")

# Example usage
count_words("sample.txt")


# Exercise 4: Convert user input string to integer with exception handling
def convert_to_integer():
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

# Example usage
convert_to_integer()


# Exercise 5: Raise an exception for negative integers in a list
def check_positive_numbers():
    try:
        numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
        if any(n < 0 for n in numbers):
            raise ValueError("Error: Negative numbers are not allowed.")
        print("Valid list:", numbers)
    except ValueError as e:
        print(e)

# Example usage
check_positive_numbers()


# Exercise 6: Compute the average of a list of integers with exception handling
def compute_average():
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        avg = sum(numbers) / len(numbers)
        print("Average:", avg)
    except ValueError:
        print("Error: Invalid input. Please enter only integers.")
    except ZeroDivisionError:
        print("Error: Cannot compute average of an empty list.")
    finally:
        print("Program execution completed.")

# Example usage
compute_average()


# Exercise 7: Write a string to a user-specified file with exception handling
def write_to_file():
    try:
        filename = input("Enter filename: ")
        content = input("Enter content to write: ")
        with open(filename, "w") as file:
            file.write(content)
        print("File written successfully. Welcome!")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
write_to_file()
