from random import randint


def generate_matrix() -> list[list[int]]:
    """
    Генерация матрицы с элементами от 0 до 255,
    количеством строчек и столбцов от 2 до 15
    """
    height, width = randint(2, 15), randint(2, 15)
    matrix = [[randint(0, 255) for _ in range(width)] for _ in range(height)]
    return matrix


def integral_view(image: list[list[int]]) -> list[list[int]]:
    """
    Расчёт матрицы интегрально представления изображения image.
    """
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
    Нахождение суммы пикселей производного прямоугольника,
    ограниченного заданными пикселями.
    """
    c = sum(image[y][x] for y in range(y2 + 1) for x in range(x2 + 1))
    a = sum(image[y][x] for y in range(y1) for x in range(x1))
    b = sum(image[y][x] for y in range(y1) for x in range(x2 + 1))
    d = sum(image[y][x] for y in range(y2 + 1) for x in range(x1))
    s = a + c - b - d
    return s
