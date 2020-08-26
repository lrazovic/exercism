from math import sqrt


def score(x: float, y: float) -> int:
    r = sqrt((x ** 2) + (y ** 2))
    return (r <= 1) * 5 + (r <= 5) * 4 + (r <= 10) * 1
