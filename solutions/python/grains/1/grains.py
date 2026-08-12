def square(number):
    # square one has one grain of rice, square two has two grains, and so on.
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    # Calculate the total number of grains on all 64 squares.
    return 2 ** 64 - 1
