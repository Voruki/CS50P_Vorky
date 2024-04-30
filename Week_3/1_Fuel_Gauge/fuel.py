# Continuously prompt the user to input a fraction until a valid fraction less than or equal to 1 is provided.
while True:
    # Prompt the user to input a fraction.
    oil_fraction = input("Fraction: ")

    try:
        # Split the fraction into numerator and denominator.
        numerator, denominator = oil_fraction.split("/")
        
        # Convert the numerator and denominator to integers.
        new_numerator = int(numerator)
        new_denominator = int(denominator)

        # Calculate the fraction.
        oil = new_numerator / new_denominator
        
        # If the fraction is less than or equal to 1, exit the loop.
        if oil <= 1:
            break

    # Handle ValueError or ZeroDivisionError exceptions.
    except ValueError or ZeroDivisionError:
        # If an exception occurs, continue to the next iteration of the loop.
        pass

# Calculate the oil percentage by rounding the oil fraction to two decimal places and multiplying by 100.
oil_percentages = int(round(oil, 2) * 100)

# Determine the oil grade based on the oil percentage.
if oil_percentages <= 1:
    print("E")
elif oil_percentages >= 99:
    print("F")
else:
    print(f"{oil_percentages}%")
