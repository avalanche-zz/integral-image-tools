"""
Function for generating matrix
"""


from random import randint


def generate() -> list[list[int]]:
    """Generates matrix of numbers (0-255) with 2..15 rows and 2..15 columns
    Returns:
        list[list[int]]: matrix
    """

    height, width = randint(2, 15), randint(2, 15)
    matrix = [[randint(0, 255) for _ in range(width)] for _ in range(height)]
    return matrix
