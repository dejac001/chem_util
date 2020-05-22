def percent_difference(x, y):
    """Return percent difference between :math:`x` and math:`y` with respect to their mean value

    >>> percent_difference(2., 1.)
    66.66666666666666
    >>> percent_difference(0, 1)
    -200.0
    >>> percent_difference(1, 1)
    0.0
    """
    return (x - y) / (x + y) * 200.

def abs_percent_difference(x, y):
    """Return absolute value of percent difference between :math:`x` and :math:`y` with respect to mean value
    
    >>> abs_percent_difference(1., 2.)
    66.6666666
    >>> abs_percent_difference(2., 1.)
    66.6666
    >>> abs_percent_difference(0, 1)
    200.00
    >>> abs_percent_difference(1, 1)
    0.0
    
    """
    return abs(percent_difference(x, y))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
