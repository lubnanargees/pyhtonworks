# Exercise 1
def calculate(a, b=10, c=None):
    if c is None:
        print(a + b)
    else:
        print(a * b * c)

# Example usage
calculate(5)          # Output: 15
calculate(5, 2)       # Output: 7
calculate(5, 2, 3)    # Output: 30


# Exercise 2
def filter_long_strings(strings):
    return list(filter(lambda s: len(s) >= 5, strings))

# Example usage
words = ["apple", "hi", "banana", "cat", "elephant"]
print(filter_long_strings(words))  # Output: ['apple', 'banana', 'elephant']


# Exercise 3
expression = "3 * 5 + 2"
result = eval(expression)
print(result)  # Output: 17


# Exercise 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    return list(filter(is_prime, numbers))

# Example usage
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(filter_primes(nums))  # Output: [2, 3, 5, 7, 11]


# Exercise 5
def convert_to_uppercase(strings):
    return list(map(str.upper, strings))

# Example usage
words = ["hello", "world", "python"]
print(convert_to_uppercase(words))  # Output: ['HELLO', 'WORLD', 'PYTHON']
