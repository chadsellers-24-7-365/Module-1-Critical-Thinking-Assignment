# ---  Pseudocode ---
# START
#     DISPLAY "Enter the first number (num1): "
#     INPUT num1
#
#     DISPLAY "Enter the second number (num2): "
#     INPUT num2
#
#     addition = num1 + num2
#     subtraction = num1 - num2
#
#     DISPLAY "Addition of", num1, "and", num2, "is:", addition
#     DISPLAY "Subtraction of", num1, "from", num2, "is:", subtraction
# END


# Get user input for two numbers
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

# Calculate addition and subtraction
addition = num1 + num2
subtraction = num1 - num2

# Print the results
print(f"Addition of {num1} and {num2} is: {addition}")
print(f"Subtraction of {num1} from {num2} is: {subtraction}")
