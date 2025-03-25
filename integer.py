#!/usr/bin/env python3

# Created By: Amara Tie

# Date: March 25, 2025

# This is a positive/negative/zero program that asks the user for an integer.


def main():
    # Enter a positive or negative number
    user_guess = int(input("Enter a postive or negative number: "))
    print("")

    # Check the user guess is correct
    if user_guess < 0:
        print(f"{user_guess} is a negative number!")
    elif user_guess == 0:
        print(f"{user_guess} is a zero.")

    elif user_guess > 0:
        print(f"{user_guess} is a positive number.")

    else:
        print("No Idea!")


if __name__ == "__main__":
    main()
