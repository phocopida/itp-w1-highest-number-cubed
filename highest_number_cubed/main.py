"""This is the entry point of the program."""


def highest_number_cubed(limit):
    n=0
    while n**3 < limit:
        n += 1
    return n-1
