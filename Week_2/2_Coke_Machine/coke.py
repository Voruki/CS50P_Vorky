# Initialize the amount_due variable to 50.
amount_due = 50

# Loop until the amount_due becomes zero or less.
while amount_due > 0:
    # Print the current amount due.
    print("Amount Due:", amount_due)
    
    # Prompt the user to insert a coin and convert the input to an integer.
    coin = int(input("Insert Coin: "))
    
    # Check if the inserted coin is a valid denomination (25, 10, or 5).
    if coin in [25, 10, 5]:
        # If the coin is valid, subtract its value from the amount_due.
        amount_due = amount_due - coin

# Calculate the absolute value of the amount_due to get the change owed.
change_owned = abs(amount_due)

# Print the amount of change owed.
print("Change Owed:", change_owned)
