# Initialize an empty dictionary to store grocery items and their counts.
grocery = {}

# Continuously prompt the user to input grocery items until an EOF (End of File) error occurs.
while True:
    try:
        # Prompt the user to input a grocery item, and convert it to lowercase for consistency.
        item = input().lower()
        
        # Check if the input item is already in the grocery dictionary.
        if item in grocery:
            # If the item is found, increment its count by 1.
            grocery[item] += 1
        else:
            # If the item is not found, add it to the grocery dictionary with a count of 1.
            grocery[item] = 1
    # Handle the EOFError exception, which occurs when the user ends the input (e.g., by pressing Ctrl+D).
    except EOFError:
        # Iterate through the keys of the grocery dictionary in sorted order.
        for key in sorted(grocery.keys()):
            # Print the count and the uppercase version of each grocery item.
            print(grocery[key], key.upper())
        # Exit the loop.
        break
