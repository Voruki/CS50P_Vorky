from datetime import date
import inflect
import sys
import operator

# Initialize the inflect engine
p = inflect.engine()

def main():
    try:
        # Prompt the user to input their date of birth
        dob = input("Date of Birth: ")
        # Check if the input date is valid
        difference = operator.sub(date.today(), date.fromisoformat(dob))
        # Convert the difference in days to words
        print(convert(difference.days))
    except ValueError:
        # Handle invalid date input
        sys.exit("Invalid date")

def convert(time):
    # Convert the time difference to minutes
    minutes = time * 24 * 60
    # Convert the minutes to words using inflect
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"

if __name__ == "__main__":
    main()
