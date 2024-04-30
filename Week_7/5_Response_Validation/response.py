import validators

def main():
    # Prompt the user to input their email address
    print(validate(input("What's your email address? ")))

def validate(s):
    # Check if the input string is a valid email address
    if validators.email(s) == True:
        return f"Valid"
    else:
        return f"Invalid"

if __name__ == "__main__":
    main()
