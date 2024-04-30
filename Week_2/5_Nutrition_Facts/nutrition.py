# Prompt the user to input a fruit.
fruit = input("Fruits: ")

# Convert the input to lowercase and remove spaces.
fruit = fruit.lower().replace(" ", "")

# Dictionary containing fruits as keys and their corresponding calorie values as values.
data = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydewmelon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweetcherries": "100",
    "tangerine": "50",
    "watermelon": "80"
}

# Check if the input fruit is in the data dictionary.
if fruit in data:
    # If the fruit is found, print its calories.
    print("Calories: " + data[fruit])
