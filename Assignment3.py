print("Exercise 1: Print the month")
month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

month = int(input("Enter the month: "))
if 1 <= month <= 12:
    print(f"Month {month} is {month_names[month - 1]}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")

print("\n")
print("Exercise 2: Cinema Ticket Price")
age = int(input("Enter your age: "))
full_price = 6.0

if age < 16:
    price = full_price / 2
elif age >= 60:
    price = full_price / 3
else:
    price = full_price

print(f"Your ticket costs £{price:.2f}")

print("\n")
print("Exercise 3: BodyMassIndex")
weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are in the 'Underweight' range.")
elif 18.5 <= bmi < 25:
    print("You are in the 'Normal' range.")
elif 25 <= bmi < 30:
    print("You are in the 'Overweight' range.")
else:
    print("You are in the 'Obese' range.")

print("\n")
print("Exercise 4: Greatest of Three Numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

greatest = max(num1, num2, num3)

print(f"The greatest number is: {greatest}")

print("\n")
print("Exercise 5: Factorial Using Loops")
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")


print("\n")
print("Exercise 6: Reverse a Number Using While Loop")
num = int(input("Enter a number: "))
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = (reverse_num * 10) + digit
    num //= 10

print(f"Reversed number is: {reverse_num}")
print("\n")
print("Exercise 7: Finding Multiples of a Number")
num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print(f"Multiples of {num}:")
for i in range(1, limit + 1):
    print(num * i)

print("\n")
print("Exercise 8: Breaking the Loop on \"done\"")
while True:
    user_input = input()
    if user_input.lower() == "done":
        print("Done")
        break
    print(user_input)


print("\n")
print("Exercise 9: FizzBuzz")
for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


print("\n")
print("Exercise 10: Pattern Printing")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
