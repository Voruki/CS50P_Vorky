# List of month names in order.
dates = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Continuously prompt the user to input a date until a valid format is provided.
while True:
    user = input("Date: ").strip()
    
    # Check if the user input contains "/" which indicates the format "month/day/year".
    if "/" in user:
        try:
            # Split the input into month, day, and year.
            m, d, y = user.split("/")
            # Convert month, day, and year to integers.
            m = int(m)
            d = int(d)
            y = int(y)
            
            # Validate the day, month, and year.
            if (d > 31 or d < 1) or (m > 12 or m < 1) or (y < 999):
                # If any of the conditions are not met, continue to the next iteration.
                continue
            
            # Print the standardized date format (YYYY-MM-DD) and exit the loop.
            print(f"{y:04}-{m:02}-{d:02}")
            break
        
        # Handle the ValueError exception if the input cannot be converted to integers.
        except ValueError:
            pass
    
    # If the user input does not contain "/", it might be in the format "month day, year".
    else:
        try:
            # Split the input into month, day, and year.
            m, d, y = user.split(" ")
            # Remove "," from the day if present.
            if "," in d:
                d = d.replace(",", "")
            
            # Convert day and year to integers.
            y = int(y)
            d = int(d)
            
            # Validate the day and year.
            if d > 31 or d < 1 or y < 999:
                # If any of the conditions are not met, continue to the next iteration.
                continue
            
            # Check if the month name is in the list of month names.
            if m.title() in dates:
                # Get the index of the month in the list.
                location = dates.index(m.title())
                # Increment the index by 1 if the month and day are equal.
                if location == d:
                    location += 1
                # Print the standardized date format (YYYY-MM-DD) and exit the loop.
                print(f"{y}-{location:02}-{d:02}")
                break
            else:
                # If the month name is not in the list, continue to the next iteration.
                continue
        
        # Handle any exceptions that may occur during the conversion or validation process.
        except:
            pass
