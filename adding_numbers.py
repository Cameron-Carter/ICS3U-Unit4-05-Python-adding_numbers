#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program lets the user add numbers

import random
import string


def main():
    # This function adds numbers however many times the user wants to

    # Input
    loops_as_string = str(input("Enter how many numbers to add: "))

    # Process and Output
    try:
        loops_as_integer = int(loops_as_string)
        loop_counter = 0
        total = 0
        if loops_as_integer > 0:
            while loops_as_integer > loop_counter:
                number_as_string = str(input("Enter a number to add: "))
                try:
                    number_as_integer = int(number_as_string)
                    loop_counter += 1
                    if number_as_integer < 0:
                        continue
                    total += number_as_integer
                except Exception:
                    print("Invalid integer")
                    continue
            print("\nThe sum of the numbers is {}".format(total))
        else:
            print("Invalid number of times")
    except Exception:
        print("{} is not an integer!".format(loops_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
