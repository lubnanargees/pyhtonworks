print("Exercise1: Print details of the student")
name = "Bob"
student_number = "ST1001"
email = "bob@gmail.com"

print(name, student_number, email)
print("\n")
print("Exercise 2: Print using escape sequences")
name = "Bob"
student_number = "ST1001"
email = "bob@gmail.com"

print(name, student_number, email, sep="\n")
print("\n")

print("Exercise 3: Perform arithmetic operations")
a = 14
b = 7
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} / {b} = {a / b}")
print("\n")

print("Exercise 4: Display numbers as steps")
for i in range(1, 6):
    print(i)
print("\n")

print("Exercise 5: Print a sentence with quotation marks")
print("\"SDK\" stands for \"Software Development Kit\", whereas")
print("\"IDE\" stands for \"Integrated Development Environment\".")
print("\n")

print("Exercise 6: Practice escape sequences")
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")
print("\n")

print("Exercise 7: Define variables and calculate sum")
num = 23
textnum = "57"
decimal = 98.3

print(type(num))
print(type(textnum))
print(type(decimal))

sum_values = num + int(textnum) + decimal
print("Sum:", sum_values)
print("Type of sum:", type(sum_values))
print("\n")

print("Exercise 8: Calculate minutes in a year")
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

total_minutes = days_in_year * hours_in_day * minutes_in_hour
print(f"Total number of minutes in a year: {total_minutes}")
print("\n")

print("Exercise 9: Greeting program")
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")
print("\n")

print("Exercise 10: Convert pounds to dollars")
pounds = float(input("Please enter amount in pounds: "))
dollar_conversion_rate = 1.3  # Example rate, change as needed
dollars = pounds * dollar_conversion_rate
print(f"£{pounds} are ${dollars}")
