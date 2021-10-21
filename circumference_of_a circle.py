# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on September 2021
# This program calculates the circumference of a circle
# With user input

import constants


def main():
    # this function calculates circumference

    # input
    radius = int(input("Enter radius of the circle here (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("circumference is {} mm.".format(circumference))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
