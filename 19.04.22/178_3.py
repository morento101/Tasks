from typing import Sequence
from time import time


def count_square_multiples_two(numbers: Sequence[int]) -> int:
    """
    Returns count of numbers from sequence which are
    squares of multiples of two
    """

    count = 0

    for number in numbers:
        number_root = number ** .5
        if not (number_root % 1) and not (number_root % 2):
            count += 1

    return count


if __name__ == '__main__':
    start = time()
    print(count_square_multiples_two(range(100)))
    print(time() - start)
