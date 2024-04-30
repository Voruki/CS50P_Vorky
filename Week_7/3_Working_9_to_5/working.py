import re

def main():
    # Prompt the user to input hours in the format "HH:MM AM/PM to HH:MM AM/PM"
    hours_input = input("Hours: ")
    
    # Call the convert function with the user input and print the result
    print(convert(hours_input))

def convert(s):
    # Define a regular expression pattern to match the input format
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    
    # Search for a match of the entire input string against the regex pattern
    match = re.search(r"^" + regex + " to " + regex + "$", s)
    
    if match:
        # If a match is found, extract the components of the "from" time and "to" time
        from_time = standardize(match.group(1), match.group(2), match.group(3))
        to_time = standardize(match.group(4), match.group(5), match.group(6))
        
        # Format the standardized times and return the result
        return f"{from_time} to {to_time}"
    else:
        # If no match is found, raise a ValueError
        raise ValueError("Invalid input format")

def standardize(hr, min, x):
    # Standardize the hour component based on the AM/PM indicator
    if hr == "12":
        hour = "00" if x == "AM" else "12"
    else:
        hour = f"{int(hr):02}" if x == "AM" else f"{int(hr)+12}"
    
    # Standardize the minute component, defaulting to "00" if not provided
    minute = "00" if min is None else f"{int(min):02}"
    
    # Return the standardized time string in "HH:MM" format
    return f"{hour}:{minute}"

if __name__ == "__main__":
    main()
