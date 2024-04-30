# Define a dictionary containing menu items as keys and their prices as values.
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize the total amount to 0.
total_amount = 0

# Continuously prompt the user to input menu items until an EOF (End of File) error occurs.
while True:
    try:
        # Prompt the user to input a menu item, and capitalize the input for consistency.
        item = input("Item: ").title()
        
        # Check if the input item is in the menu dictionary.
        if item in menu:
            # If the item is found, add its price to the total amount.
            total_amount += menu[item]
            
            # Print the total amount formatted with two decimal places.
            print("Total: $", end="")
            print("{:.2f}".format(total_amount))
    
    # Handle the EOFError exception, which occurs when the user ends the input (e.g., by pressing Ctrl+D).
    except EOFError:
        # Print a newline character to ensure a clean output.
        print()
        # Exit the loop.
        break
