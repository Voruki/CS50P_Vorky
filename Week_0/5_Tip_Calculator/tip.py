# Define the main function to calculate the tip amount.
def main():
    # Prompt the user for the cost of the meal and convert it to a float value.
    dollars = dollars_to_float(input("How much was the meal? "))
    
    # Prompt the user for the desired tip percentage and convert it to a float value.
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip amount by multiplying the meal cost by the tip percentage.
    tip = dollars * percent
    
    # Print the calculated tip amount.
    print(f"Leave ${tip:.2f}")

# Define a function to convert a string representing a dollar amount to a float value.
def dollars_to_float(d):
    # Remove the dollar sign from the string and convert it to a float.
    x = d.strip("$")
    return float(x)

# Define a function to convert a string representing a percentage to a float value.
def percent_to_float(p):
    # Remove the percentage sign from the string and convert it to a float,
    # then divide by 100 to get the decimal representation of the percentage.
    y = p.strip("%")
    return float(y) / 100

# Call the main function to execute the program.
main()
