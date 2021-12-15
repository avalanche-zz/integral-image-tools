def generate_matrix() -> list[list[int]]:
    ...


def integral_view(image: list[list[int]]) -> list[list[int]]:
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
    ...
