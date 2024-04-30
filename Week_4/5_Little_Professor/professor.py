from random import randint

def main():
    points = 0
    level = get_level()

    # Iterate over 10 questions.
    for i in range(10):
        # Initialize a counter to keep track of wrong answers.
        counter = 0
        # Generate random numbers for the addition problem.
        fNumber = generate_integer(level)
        sNumber = generate_integer(level)
        answer = fNumber + sNumber

        # Loop until the user enters a correct answer or exhausts all attempts.
        while True:
            try:
                # Prompt the user to input their answer and convert it to an integer.
                check = int(input("{0} + {1} = ".format(fNumber, sNumber)))
            except ValueError:
                # If the user input is not an integer, increment the counter and continue the loop.
                counter += 1
                continue
            else:
                # If the user input is not equal to the correct answer.
                if answer != check:
                    print("EEE")
                    counter += 1
                    # If the user enters three wrong answers, reveal the correct answer and break the loop.
                    if counter == 3:
                        print("{0} + {1} = {2}".format(fNumber, sNumber, answer))
                        break
                # If the user input is correct, increment the points and break the loop.
                else:
                    points += 1
                    break

    # Print the final score.
    print(f"Score: {points}")


def get_level():
    while True:
        try:
            # Prompt the user to input the level and convert it to an integer.
            temp = int(input("Level: "))
        except ValueError:
            # If the input cannot be converted to an integer, continue to the next iteration.
            continue
        else:
            # Check if the input is a valid level (1, 2, or 3).
            if temp not in [1, 2, 3]:
                continue
            else:
                return temp


def generate_integer(level):
    # Generate a random integer based on the selected level.
    if level == 1:
        return int(randint(0, 10))
    elif level == 2:
        return int(randint(10, 99))
    else:
        return int(randint(100, 999))


if __name__ == "__main__":
    main()
