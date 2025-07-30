# --- Basic Calculator Program ---

# 1. Get input for the first number
# We use float() to allow for decimal numbers.
# The input() function always returns a string, so conversion is necessary.
try:
    num1 = int(input("Enter the first number: "))
except ValueError:
    print("Invalid input for the first number. Please enter a valid number.")
    exit() # Exit the program if input is not a number

# 2. Get input for the second number
try:
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input for the second number. Please enter a valid number.")
    exit() # Exit the program if input is not a number

# 3. Get input for the operation
operation = input("Enter the operation (+, -, *, /): ")

# 4. Perform the operation based on user input
result = None # Initialize result to None

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Basic error handling for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero!")
        exit() # Exit the program gracefully
else:
    # Handle invalid operations
    print("Error: Invalid operation. Please use +, -, *, or /.")
    exit() # Exit the program

# 5. Print the result in a user-friendly format
# Check if result was calculated (i.e., not None due to an error)
if result is not None:
    # Using an f-string for clear output formatting
    print(f"Result: {num1} {operation} {num2} = {result}")

# --- End of Basic Calculator Program ---