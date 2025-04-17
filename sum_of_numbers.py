#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 8, 2025
# This program catches erroneous input,
# It then uses a while loop to add all the numbers
# from 0 to that integer and displays the sum


def main():
    # initialization
    counter = 0

    # get the user's input
    user_string = input("Enter a number: ")
    try:
        user_integer = int(user_string)
        if user_integer > 0:
            while counter < user_integer:
                print("{} time through loop".format(counter))
                counter = counter + 1
            print(
                "The sum of the numbers from 0 to {} = {}".format(counter, user_integer)
            )
        else:
            print("{} is not a positive integer".format(user_integer))

    except Exception:
        print("{} is not a valid input".format(user_string))


if __name__ == "__main__":
    main()
