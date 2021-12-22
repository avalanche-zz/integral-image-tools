"""
Functions for maintaining integral image
"""


def integral_view(image: list[list[int]]) -> list[list[int]]:
    """
    Calculate matrix of integral image for "image"
    """
    # Checking "image"
    if not isinstance(image, list):
        raise ValueError("\"image\"'s must be a list")
    else:
        for index, item in enumerate(image):
            if index == len(image) - 1:
                pass
            else:
                if len(image[index]) != len(image[index + 1]):
                    raise ValueError("items of \"image\" must be of the same length")
            if not isinstance(item, list):
                raise ValueError("items of \"image\" must be lists")
            for num in item:
                if not isinstance(num, int):
                    raise ValueError("items of items of \"image\" must be integers")
                if num < 0 or num > 255:
                    raise ValueError("items of items of \"image\" must be integers between 0 and 255") 

    height, width = len(image), len(image[0])
    integral_image = [[0] * width for _ in range(height)]
    for y in range(height):
        summation = 0
        for x in range(width):
            summation += image[y][x]
            integral_image[y][x] = summation
            if y > 0:
                integral_image[y][x] += integral_image[y - 1][x]
    return integral_image


def rect_sum(image: list[list[int]], x1: int, y1: int, x2: int, y2: int) -> int:
    """
    Calculate sum of pixels of a random rectangle with given border points
    """
    # Checking "image"
    if not isinstance(image, list):
        raise ValueError("\"image\"'s must be a list")
    else:
        for index, item in enumerate(image):
            if index == len(image) - 1:
                pass
            else:
                if len(image[index]) != len(image[index + 1]):
                    raise ValueError("items of \"image\" must be of the same length")
            if not isinstance(item, list):
                raise ValueError("items of \"image\" must be lists")
            for num in item:
                if not isinstance(num, int):
                    raise ValueError("items of items of \"image\" must be integers")
                if num < 0 or num > 255:
                    raise ValueError("items of items of \"image\" must be integers between 0 and 255") 

    # Checking coordinates
    top_left_border = (x1, y1)
    bottom_right_border = (x2, y2)
    for coordinate in top_left_border:
        if not isinstance(coordinate, int) or coordinate < 0:
            raise ValueError("border coordinate(s) must be positive integer(s)")
    for coordinate in bottom_right_border:
        if not isinstance(coordinate, int) or coordinate < 0:
            raise ValueError("border coordinate(s) must be positive integer(s)")
    if x1 > len(image[0]) or x2 > len(image[0]):
        raise ValueError("x1 or x2 must not be greater than the number of the matrix columns")
    if y1 > len(image) or y2 > len(image):
        raise ValueError("y1 or y2 must not be greater than the number of the matrix rows")
    if x1 > x2 or y1 > y2:
        raise ValueError("top-left border coordinate must not be greater than bottom-right border coordinates")

    c = sum(image[y][x] for y in range(y2 + 1) for x in range(x2 + 1))
    a = sum(image[y][x] for y in range(y1) for x in range(x1))
    b = sum(image[y][x] for y in range(y1) for x in range(x2 + 1))
    d = sum(image[y][x] for y in range(y2 + 1) for x in range(x1))
    s = a + c - b - d
    return s

image = [
    [32, 39, 2, 20, 8, 13, 2, 5, 3],
    [15, 14, 11, 12, 13, 14, 5, 20, 8],
    [7, 14, 1, 0, 14, 6, 5, 13, 8],
    [5, 13, 10, 13, 8, 1, 12, 20, 1],
    [0, 2, 12, 20, 15, 7, 19, 30, 48],
    [23, 54, 11, 10, 76, 30, 44, 11, 22],
    [11, 25, 77, 22, 15, 42, 23, 5, 12],
    [45, 33, 65, 3, 17, 8, 90, 6, 48],
    [25, 1, 54, 54, 88, 6, 13, 56, 23],
    [13, 8, 9, 23, 0, 78, 4, 42, 11],
    [28, 98, 12, 45, 18, 34, 7, 28, 75],
    [79, 14, 6, 43, 33, 89, 14, 41, 28],
    [21, 32, 14, 13, 6, 69, 68, 60, 26],
    [34, 76, 98, 24, 8, 5, 17, 18, 13]
]

print(rect_sum(image, 3, 5, 5, 8))