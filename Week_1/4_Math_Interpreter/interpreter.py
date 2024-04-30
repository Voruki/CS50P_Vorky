# Prompt the user to input an expression and split it into three parts: x, y (operator), and z.
expression = input("Expression: ")
x, y, z = expression.split(" ")

# Convert x and z to floating-point numbers.
new_x = float(x)
new_z = float(z)

# Check the operator (y) and perform the corresponding operation.
if y == "+":
    result = new_x + new_z
elif y == "-":
    result = new_x - new_z
elif y == "*" or y == "x" or y == "X":
    result = new_x * new_z
elif y == "/":
    result = new_x / new_z
else:
    # If the operator is not recognized, set the result to an error message.
    result = "Please try again later!"

# Print the result rounded to one decimal place.
print(round(result, 1))
