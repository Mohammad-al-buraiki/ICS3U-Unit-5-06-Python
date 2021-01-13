# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is for rounding numbers


def rounding(user_input, times):
    # pass by referrance
    user_input[0] = user_input[0]*10**times[0]
    user_input[0] = user_input[0] + 0.5
    user_input[0] = int(user_input[0])
    user_input[0] = user_input[0]/10**times[0]


def main():
    number1 = []
    number2 = []

    user_input = float(input("Enter the number:"))
    times = int(input("Enter how many places you want to round:"))
    number1.append(user_input)
    number2.append(times)
    rounding(number1, number2)
    print("{0}.".format(number1[0]))


if __name__ == "__main__":
    main()
