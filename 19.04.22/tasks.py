from typing import Sequence
from typing import List
from time import time


def validate_sequence_input(func):
    def wrapper(*args, **kwargs):
        error = TypeError(f'Invalid type, in {func.__name__} you can pass only sequences')
        types = (list, tuple, set, range)

        for arg in args:
            if type(arg) not in types:
                raise error

        for kwarg_value in kwargs.values():
            if type(kwarg_value) not in types:
                raise error
            
        return func(*args, **kwargs)
    return wrapper


def validate_int_input(func):
    def wrapper(*args, **kwargs):
        error = TypeError(f'Invalid type, in {func.__name__} you can pass only int, float type values')
        types = (int, float)

        for arg in args:
            if type(arg) not in types:
                raise error

        for kwarg_value in kwargs.values():
            if type(kwarg_value) not in types:
                raise error
            
        return func(*args, **kwargs)
    return wrapper



@validate_sequence_input
def count_multiples_of_three_not_five(numbers: Sequence[int]) -> int:
    """
    Return amount of numbers from sequence which are 
    multiples of three but not multiples of five
    """
    count = 0

    for number in numbers:
        if not number % 3 and number % 5:
            count += 1

    return count


@validate_sequence_input
def count_square_multiples_two(numbers: Sequence[int]) -> int:
    """
    Returns count of numbers from sequence which are
    squares of multiples of two
    """
    count = 0

    for number in numbers:
        if number < 0:
            raise ValueError(f"Can't calculate square root from negative number {number}")

        number_root = number ** .5
        if not (number_root % 1) and not (number_root % 2):
            count += 1

    return count


@validate_int_input
def pythagorean_triples(n: int) -> List[tuple]:
    """
    Returns list of tuples with all pythagorean triples which satisfy
    following equations: a^2 + b^2 = c^2 and a <= b <= c <= n
    """
    res = []
    domain = range(1, n+1)
    n_square = n ** 2

    for a in domain:
        for b in domain:
            c = a**2 + b**2
            if c <= n_square:
                if not c**.5 % 1:
                    res.append((a, b, int(c**.5)))

    return res


if __name__ == '__main__':
    start = time()
    count_multiples_of_three_not_five(range(100))
    print(time() - start)

    start = time()
    count_square_multiples_two(range(100))
    print(time() - start)

    start = time()
    pythagorean_triples(50)
    print(time() - start)
