import re

def main():
    # Ask user for input and print the result of the validation
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression pattern to match IPv4 address
    regex = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    
    # Use regex to search for the pattern in the input IP address
    res = re.search(regex, ip)
    
    # If no match is found, return False
    if not res:
        return False

    # If there are four groups in the match (each representing an octet)
    if len(res.groups()) == 4:
        # Loop through each group
        for gp in res.groups():
            try:
                # Convert the group to an integer
                gp = int(gp)
            except ValueError:
                # If conversion fails (e.g., not an integer), return None
                return None

            # Check if the integer value of the octet is within the valid range
            if gp >= 0 and gp <= 255:
                # If within range, continue to the next octet
                pass
            else:
                # If not within range, return False
                return False
        # If all octets are valid, return True
        return True
    else:
        # If there are not exactly four groups, return False
        return False

if __name__ == "__main__":
    main()
