import requests
import sys

# Check if the number of command-line arguments is correct.
if len(sys.argv) == 2:
    # Convert the command-line argument to a float number.
    try:
        user_input = float(sys.argv[1])
    except ValueError:
        # If the command-line argument is not a number, print an error message and exit.
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    # If the number of command-line arguments is incorrect, print an error message and exit.
    print("Missing command-line argument")
    sys.exit(1)

try:
    # Call the CoinDesk API to get the current Bitcoin price in USD.
    answer = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    # Extract the Bitcoin price in USD and convert it to a float number.
    price = float(answer["bpi"]["USD"]["rate_float"])
    # Calculate the value of the given amount of Bitcoin in USD.
    value_in_usd = price * user_input
    # Print the value in USD with 4 decimal places and thousands separators.
    print(f"${value_in_usd:,.4f}")
    sys.exit(0)
except (requests.RequestException, ValueError):
    # Handle errors such as network issues or invalid JSON response.
    print("Error")
    sys.exit(1)
