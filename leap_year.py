#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program tells a user if their inputted year is a leap year


def main():
    # This function determines if the user's year is a leap year

    # Input
    year_as_string = input("Enter a year after year 0: ")
    print("")

    # Process and Output
    try:
        year_as_integer = int(year_as_string)
        if year_as_integer % 4 == 0:
            if year_as_integer % 100 == 0:
                if year_as_integer % 400 == 0:
                    print("{0} is a leap year.".format(year_as_integer))
                else:
                    print("{0} is not a leap year.".format(year_as_integer))
            else:
                print("{0} is a leap year.".format(year_as_integer))
        else:
            print("{0} is not a leap year.".format(year_as_integer))

    except Exception:
        print("Please input a valid number.")

    print("\nDone.")


if __name__ == "__main__":
    main()
