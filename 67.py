import sys


def firstInput():
    global count_six
    global count_seven

    while True:
        user_input = input(
            "Type a valid input ('6' or '7'). Type 'q' to quit:\n"
        ).strip()

        if user_input == "q":
            print("Exiting the function...")
            print("Number of 6s:", count_six)
            print("Number of 7s:", count_seven)
            sys.exit()

        if user_input == "6":
            print("You entered 6!")
            count_six += 1
        elif user_input == "7":
            print("You entered 7!")
            count_seven += 1
        else:
            print("Invalid input. Try again.")


# Initializing the counters
count_six = 0
count_seven = 0

firstInput()
