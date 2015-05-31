"""This is the main module with a lot of statistical functions."""

def mean(*args):
    """Returns the mean of args.

    *args -- sequence to unpack or separate numerical arguments
    >>> mean(1,2,3)
    2.0
    >>> mean(*[-3,-4,-8])
    -5.0
    >>> mean(*range(1001))
    500.0
    >>> mean()
    Traceback (most recent call last):
    TypeError: needs at least one argument
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
        raise TypeError("needs at least one argument")

def median(*args):
    """Returns the median of args.

    *args -- sequence to unpack or separate numerical arguments
    >>> median(0,2,3,10)
    2.5
    >>> median(13,42,666)
    42
    >>> median('a string', 'string', 'a string')
    'a string'
    >>> median()
    Traceback (most recent call last):
    TypeError: needs at least one argument
    """
    try:
        args = sorted(list(args))
        n = len(args)
        if n%2==0:
            return (args[(n//2)-1]+args[n//2])/2
        else:
            return args[n//2]
    except IndexError:
        raise TypeError("needs at least one argument")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
