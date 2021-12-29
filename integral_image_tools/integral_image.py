"""
Functions for calculating integral image and
sum of pixels of a rectangle with given border points
"""


def integral_view(image: list[list[int]]) -> list[list[int]]:
    """Calculates matrix of integral image for "image"

    :param image: matrix of integers from 0 to 255
    :type image: list[list[int]]
    :return: matrix of integral image
    :rtype: list[list[int]]
    """
    # Checking "image"
    if not isinstance(image, list):
        raise ValueError("\"image\"'s must be a list")
    else:
        for index, item in enumerate(image):
            if not isinstance(item, list):
                raise ValueError("items of \"image\" must be lists")
            for num in item:
                if not isinstance(num, int) or num < 0 or num > 255:
                    raise ValueError(
                        "items of items of \"image\" must be integers between 0 and 255")
            if index == len(image) - 1:
                pass
            else:
                if len(image[index]) != len(image[index + 1]):
                    raise ValueError(
                        "items of \"image\" must be of the same length")

    # Calculating matrix
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


def rect_sum(rect: list[list[int]], x1: int, y1: int, x2: int, y2: int) -> int:
    """Calculates sum of pixels of a rectangle within given borders

    :param rect: matrix of integers
    :type rect: list[list[int]]
    :param x1: top left border X coordinate
    :type x1: int
    :param y1: top left border Y coordinate
    :type y1: int
    :param x2: bottom right X coordinate
    :type x2: int
    :param y2: bottom right Y coordinate
    :type y2: int
    :return: sum of integers
    :rtype: int
    """
    # Checking "image"
    if not isinstance(rect, list):
        raise ValueError("\"image\"'s must be a list")
    else:
        for index, item in enumerate(rect):
            if not isinstance(item, list):
                raise ValueError("items of \"image\" must be lists")
            for num in item:
                if not isinstance(num, int):
                    raise ValueError(
                        "items of items of \"image\" must be integers")
            if index == len(rect) - 1:
                pass
            else:
                if len(rect[index]) != len(rect[index + 1]):
                    raise ValueError(
                        "items of \"image\" must be of the same length")

    # Checking coordinates
    top_left_border = (x1, y1)
    bottom_right_border = (x2, y2)
    for coordinate in top_left_border:
        if not isinstance(coordinate, int) or coordinate < 0:
            raise ValueError(
                "border coordinate(s) must be positive integer(s)")
    for coordinate in bottom_right_border:
        if not isinstance(coordinate, int) or coordinate < 0:
            raise ValueError(
                "border coordinate(s) must be positive integer(s)")
    if x1 > len(rect[0]) - 1 or x2 > len(rect[0]) - 1:
        raise ValueError(
            "x1 and/or x2 must not be greater than the number of the matrix columns")
    if y1 > len(rect) - 1 or y2 > len(rect) - 1:
        raise ValueError(
            "y1 and/or y2 must not be greater than the number of the matrix rows")
    if x1 > x2 or y1 > y2:
        raise ValueError(
            "top-left border coordinates must not be greater than bottom-right border coordinates")

    # Calculatins sum
    c = sum(rect[y][x] for y in range(y2 + 1) for x in range(x2 + 1))
    a = sum(rect[y][x] for y in range(y1) for x in range(x1))
    b = sum(rect[y][x] for y in range(y1) for x in range(x2 + 1))
    d = sum(rect[y][x] for y in range(y2 + 1) for x in range(x1))
    s = a + c - b - d
    return s
