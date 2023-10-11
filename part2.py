# ---  Pseudocode ---
# START
#     DISPLAY "Enter the first number (num1): "
#     INPUT num1
#
#     DISPLAY "Enter the second number (num2): "
#     INPUT num2
#
#     multiplication = num1 * num2
#
#     IF num2 IS NOT EQUAL TO 0 THEN
#         division = num1 / num2
#         DISPLAY "Multiplication of", num1, "and", num2, "is:", multiplication
#         DISPLAY "Division of", num1, "by", num2, "is:", division
#     ELSE
#         DISPLAY "Division by zero is not allowed!"
#     END IF
# END
#

# Get user input for two numbers
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

# Calculate multiplication and division
multiplication = num1 * num2

# Check if the denominator (num2) is zero to avoid a ZeroDivisionError
if num2 == 0:
    print("Division by zero is not allowed!")
else:
    division = num1 / num2
    # Print the results
    print(f"Multiplication of {num1} and {num2} is: {multiplication}")
    print(f"Division of {num1} by {num2} is: {division}")
