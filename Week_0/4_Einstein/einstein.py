# Prompt the user to input the mass value (should be an integer) and store it in the variable 'mass'.
mass = input("Please input the mass value (integer only) : ")

# Convert the input 'mass' to an integer using the 'int()' function,
# then calculate the energy using the formula E = mc^2 and print the result.
# Note: 'pow()' function calculates the power of the first argument (300000000) to the second argument (2).
print(int(mass) * pow(300000000, 2))
