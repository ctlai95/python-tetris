import operator


def add(a, b):
    """Calculates the element-wise addition of two tuples and returns the result"""
    return tuple(map(operator.add, a, b))


def subtract(a, b):
    """Calculates the element-wise subtraction of two tuples and returns the result"""
    return tuple(map(operator.sub, a, b))
