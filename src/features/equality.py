EPSILON = 0.00001

def is_approximately_equal(number1: float, number2: float) -> bool:
    return abs(number1 - number2) < EPSILON