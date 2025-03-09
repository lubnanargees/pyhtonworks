
#Exercise1:read a file and display its contents
file1=open("C:\\Users\\User\\Desktop\\sample.txt",'r')
print(file1.read())

#Exercise 2: To copy the contents of one file to another file
# Open the source file in read mode and destination file in write mode
with open("C:\\Users\\User\\Desktop\\sample.txt", "r") as source_file, open("C:\\Users\\User\\Desktop\\sample2.txt", "w") as dest_file:
    # Read content from source file and write to destination file
    dest_file.write(source_file.read())

print("File copied successfully!")

#Exercise 3: Write a Python program to read the content of a file
# and count the total number of words in that file.

# Function to count words in a file
def count_words_in_file(filename):
    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            # Read the file content
            content = file.read()

        # Split the content into words
        words = content.split()

        # Count the total number of words
        word_count = len(words)

        print(f"Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the file path.")


file_name = "C:\\Users\\User\\Desktop\\sample.txt"
count_words_in_file(file_name)

# Exercise 4: input a string and convert it to an integer (Use try-except blocks )
# Function to safely convert a string to an integer
def convert_to_integer():
    user_input = input("Enter a string to convert to an integer: ")

    try:
        # Attempt to convert the input to an integer
        number = int(user_input)
        print(f"Conversion successful! The integer is: {number}")
    except ValueError:
        # Handle the exception if the string cannot be converted to an integer
        print("Error: The input is not a valid integer. Please enter a valid numeric string.")

convert_to_integer()


# Exercise 5: Function to check for negative integers in the list
# Function to check for negative integers in the list
def check_for_negatives():
    try:
        # Prompt the user to input a list of integers
        user_input = input("Enter a list of integers separated by spaces: ")

        # Convert the input string into a list of integers
        numbers = list(map(int, user_input.split()))

        # List to store negative numbers
        negative_numbers = []

        # Check for negative integers
        for number in numbers:
            if number < 0:
                # Add the negative number to the list
                negative_numbers.append(number)

        # If there are any negative numbers, raise an exception
        if negative_numbers:
            raise ValueError(f"Negative numbers found: {negative_numbers}")

        print("All numbers are non-negative!")
    except ValueError as e:
        # Handle the case when the input contains negatives or invalid numbers
        print(f"Error: {e}")


check_for_negatives()

#Exercise 6: Input a list of integers and compute the average of those integers.
# Function to compute the average of a list of integers
def compute_average():
    try:
        # Prompt the user to input a list of integers
        user_input = input("Enter a list of integers separated by spaces: ")

        # Convert the input string into a list of integers
        numbers = list(map(int, user_input.split()))

        # Ensure there is at least one number to compute the average
        if len(numbers) == 0:
            raise ValueError("The list is empty. Cannot compute the average.")

        # Compute the average
        average = sum(numbers) / len(numbers)
        print(f"The average of the entered integers is: {average}")
    except ValueError as e:
        # Handle invalid inputs (e.g., non-integer values or empty input)
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        # This block executes regardless of exceptions
        print("The program has finished running.")


compute_average()
#Exercise 7 :Input a filename and writes a string to that file.
# Function to write a string to a file specified by the user
def write_to_file():
    try:
        # Prompt the user for a filename
        filename = input("Enter the filename: ")

        # Prompt the user for the string to write to the file
        content = input("Enter the string to write to the file: ")

        # Open the file in write mode and write the content
        with open(filename, 'w') as file:
            file.write(content)

        # Print a welcome message if no exception occurred
        print(f"Welcome! The content was successfully written to '{filename}'.")
    except Exception as e:
        # Handle exceptions (e.g., invalid filename or permission issues)
        print(f"An error occurred: {e}")


write_to_file()
