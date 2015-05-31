"""This is the main module with a lot of statistical functions."""

def mean(*args):
    """Returns the mean of args.

    *args -- sequence to unpack, or separate numerical arguments
    >>> mean(1,2,3)
    2.0
    >>> mean(*[3,4,8])
    5.0
    >>> mean(*range(1001))
    500.0
    >>> mean()
    Traceback (most recent call last):
    TypeError: *args cannot be empty
    >>> mean('string')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +=: 'int' and 'str'
    """
    try:
        running_sum = 0
        for x in args:
            running_sum += x
        return running_sum/len(args)
    except ZeroDivisionError:
        raise TypeError("*args cannot be empty")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
