from math import inf
EPSILON = 0.00001

def is_approximately_equal(number1: float, number2: float) -> bool:
    if abs(number1) == inf or abs(number2) == inf:
        return number1 == number2
    return abs(number1 - number2) < EPSILON