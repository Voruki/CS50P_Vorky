# Define the main function.
def main():
    # Prompt the user to input the current time.
    answer = input("What time is it? ")
    
    # Call the convert function to convert the time to decimal format.
    time = convert(answer)

    # Check the time range and print the corresponding meal time message.
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >=12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

# Define the convert function to convert time in HH:MM format to decimal format.
def convert(time):
    # Split the time string into hours and minutes.
    hours, minutes = time.split(":")
    
    # Convert minutes to decimal format (e.g., 30 minutes becomes 0.5).
    new_minute = float(minutes) / 60
    
    # Convert hours and add the decimal minutes to get the time in decimal format.
    return float(hours) + new_minute

# Check if the script is being run directly.
if __name__ == "__main__":
    # If so, call the main function to start the program.
    main()
