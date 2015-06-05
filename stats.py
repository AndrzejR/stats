"""This is the main module with a lot of statistical functions."""

def mean(data):
    """Returns the mean of data.

    data -- a sequence of numerical arguments
    >>> mean((1,2,3))
    2.0
    >>> mean([-3,-4,-8])
    -5.0
    >>> mean(range(1001))
    500.0
    >>> mean()
    Traceback (most recent call last):
    TypeError: mean() missing 1 required positional argument: 'data'
    >>> mean('string')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +=: 'int' and 'str'
    """
    try:
        running_sum = 0
        for x in data:
            running_sum += x
        return running_sum/len(data)
    except ZeroDivisionError:
        raise TypeError("needs at least one argument")

def median(data):
    """Returns the median of data.

    data -- sequence to unpack or separate numerical arguments
    >>> median((0,2,3,10))
    2.5
    >>> median([13,42,666])
    42
    >>> median(['a string', 'string', 'a string'])
    'a string'
    >>> median()
    Traceback (most recent call last):
    TypeError: median() missing 1 required positional argument: 'data'
    """
    try:
        data = sorted(list(data))
        n = len(data)
        if n%2==0:
            return (data[(n//2)-1]+data[n//2])/2
        else:
            return data[n//2]
    except IndexError:
        raise TypeError("needs at least one argument")

def mode(*data):
    raise NotImplementedError

def sum_of_squares(data):
    """Returns the sum of squared distances from the mean.

    >>> sum_of_squares([1,2,6])
    14.0
    """
    mean = sum(data)/len(data)
    return sum((x-mean)**2 for x in data)

def variance_p(data):
    """Returns the population variance.

    >>> variance_p([1,3,5,7,14])
    20.0
    """
    pop_mean = mean(data)
    return sum_of_squares(data)/len(data)

def variance_s(data):
    """Returns the sample variance.

    >>> variance_s([9,8,5,1,1])
    14.2
    """
    pop_mean = mean(data)
    return sum_of_squares(data)/(len(data)-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
