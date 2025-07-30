# Task 1: Perform Basic Mathematical Operations

# Step 1: Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform the basic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Division with zero-check
if num2 != 0:
    division = num1 / num2


# Step 3: Display results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
