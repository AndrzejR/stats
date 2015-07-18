"""This is the main module with a lot of statistical functions."""

from math import sqrt, ceil
import random

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
    >>> median(range(10))
    4.5
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

def mode(data):
    """Returns the mode of a unimodal distribution.

    >>> mode([1,2,3,4,4,4,4])
    4
    >>> mode([-10,-10,-10,13,42,256])
    -10
    >>> mode(['a', 'a', 'b', 'b', 'c', 'c', 'a'])
    'a'
    """
    frequencies = {}
    maximum = 0
    mode = None

    for x in data:
        try:
            frequencies[x] += 1
        except KeyError:
            frequencies[x] = 1
        if frequencies[x] > maximum:
            mode = x
            maximum = frequencies[x]

    return mode


def sum_of_squares(data):
    """Returns the sum of squared distances from the mean.

    >>> sum_of_squares([1,2,6])
    14.0
    """
    m = mean(data)
    return sum((x-m)**2 for x in data)

def pvar(data):
    """Returns the population variance.

    >>> pvar([1,3,5,7,14])
    20.0
    """
    return sum_of_squares(data)/len(data)

def svar(data):
    """Returns the sample variance.

    >>> svar([9,8,5,1,1])
    14.2
    """
    return sum_of_squares(data)/(len(data)-1)

def psd(data):
    """Returns the population standard deviation.

    >>> round(psd([1,2,6]), 4)
    2.1602
    """
    return sqrt(pvar(data))

def ssd(data):
    """Returns the sample standard deviation of the data.

    >>> round(ssd([0,2,4,8]), 4)
    3.4157
    """
    return sqrt(svar(data))

def z_score(x, mean, sd):
    """Return the z-score given the datapoint, mean, and standard deviation.

    >>> round(z_score(83,82.2,5), 2)
    0.16
    """
    return (x-mean)/sd

def box_plot(data):
    """Doesn't do much atm..."""
    raise NotImplementedError
    Q2 = median(data)
    Q1 = median(data[:len(data)/2])
    Q3 = median(data[len(data)/2:])

# bug - what about the median for even sets?
def quantile(data, q, k):
    """Returns the k-th q-quantile of data.

    Uses the inclusive, Tukey's method.
    >>> quantile([1,2,3,4,5], 2, 1)
    3
    >>> quantile(range(10), 4, 1)
    2
    >>> quantile(range(10), 4, 3)
    7
    >>> quantile(range(9), 4, 1)
    2
    >>> quantile(range(9), 4, 3)
    6
    """
    rank = ceil((len(data)/q) * k)
    return data[rank-1]

def iqr(data):
    """Return the Inter Quartile Range of the data.

    >>> iqr(range(10))
    5
    """
    return quantile(data, 4, 3) - quantile(data, 4, 1)

def factorial(n):
    """Return the factorial of a natural number.

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def permute(n, k):
    """Return the number of possible permutations of k from n.

    >>> permute(4, 4)
    24
    >>> permute(5, 2)
    20
    >>> permute(6, 1)
    6
    """
    return int(factorial(n)/factorial(n-k))

def combine(n, k):
    """Return the number of combinations w/o repetition of k from n.

    >>> combine(4, 4)
    1
    >>> combine(5, 2)
    10
    >>> combine(6, 1)
    6
    """
    return int(permute(n, k)/factorial(k))

def mad(data):
    """Returns Mean Absolute Deviation of the data.

    >>> mad([1,2,3,4])
    1.0
    >>> mad([2,2,2])
    0.0
    """
    return sum(abs(mean(data)-x) for x in data)/len(data)

def emp_rule(mean, sd, less_than=None, greater_than=None):
    """Khan Academy Empirical Rule solver. Assumes 68-95-99.7

    >>> emp_rule(114, 8.2, less_than=122.2)
    84
    >>> emp_rule(28, 3.8, less_than=39.8)
    99.85
    >>> emp_rule(19.4, 1.3, less_than=20.7)
    84
    >>> emp_rule(30, 3, greater_than=24)
    97.5
    >>> emp_rule(17.7, 2.8, greater_than=20.5, less_than=26.1)
    15.85
    """
    if less_than and not greater_than:
        z = int(z_score(less_than, mean, sd))

        if z==3:
            return 99.85
        elif z==2:
            return 97.5
        elif z==1:
            return 84
        elif z==0:
            return 50

    elif greater_than and not less_than:
        z = abs(int(z_score(greater_than, mean, sd)))

        if z==3:
            return 99.85
        elif z==2:
            return 97.5
        elif z==1:
            return 84
        elif z==0:
            return 50

    else:
        lower_z = int(z_score(greater_than, mean, sd))
        higher_z = int(z_score(less_than, mean, sd))


# how well does s approximate sigma depending on sample size?

def gen_dataset(size=100000, max=1000):
    dataset = []
    for _ in range(size):
        dataset.append(random.randint(1,max))
    return dataset

def get_samples(dataset, size=20, number=1000):
    samples = []
    for _ in range(number):
        samples.append(random.sample(dataset, size))
    return samples

def calc_app():
    data = gen_dataset()
    mu = mean(data)
    sigma = psd(data)
    for sample_size in range(2, 31):
        samples = get_samples(data, size=sample_size)
        ssds = map(ssd, samples)
        differences = []
        for sample_sd in ssds:
            differences.append(sigma - sample_sd)
        average_diff = mean(differences)
        print('sample size = ' + str(sample_size) + ', average difference = ' + str(average_diff))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
