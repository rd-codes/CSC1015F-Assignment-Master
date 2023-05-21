# A program to plot a graph  of a function entered by the user, using asterisks and underscores.
# 17 May 2021

import math

# Convert string function to a function that takes numbers in range {-10,10} and store the output as a list


def axis(f_x):
    x_axis = "-"
    y_axis = "|"
    # sketch the graph on x_y plane
    for y in range(10, -11, -1):
        for x in range(-10, 11):
            y_value = round(eval(f_x))    # Temporarily store y value at x
            if y == y_value:
                print("*", end="")
            elif y == 0 and x == 0:
                print("+", end="")
            elif y == 0:
                print(x_axis, end="")
            elif x == 0:
                print(y_axis, end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    f = input("Enter a function f(x):\n")
    axis(f)
