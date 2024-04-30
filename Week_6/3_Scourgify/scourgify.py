import os
import sys
import csv

# Header of the new CSV file
file_headers = ["first", "last", "house"]

# Function to check command-line arguments
def check_command_line():
    if len(sys.argv) != 3:
        sys.exit("Invalid number of command-line arguments")

# Function to normalize data from the old CSV file
def normalize_data(oldfile):
    db = []
    reader = csv.DictReader(oldfile)

    for each in reader:
        temp = {}
        # Split the name into first and last names
        temp["last"], temp["first"] = each["name"].split(",")
        # Remove white spaces
        temp["first"] = temp["first"].strip()
        temp["last"] = temp["last"].strip()
        temp["house"] = each["house"]
        db.append(temp)
    return db

# Function to create a new CSV file with normalized data
def create_csv(data, filename):
    with open(filename, "w", encoding="UTF8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=file_headers)
        writer.writeheader()
        writer.writerows(data)

# Main function
def main():
    check_command_line()
    try:
        file = open(sys.argv[1], "r", encoding="utf-8")
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} not found")

    # Clean the data
    data = normalize_data(file)

    # Create a new file
    create_csv(data, sys.argv[2])

    file.close()

if __name__ == "__main__":
    main()
