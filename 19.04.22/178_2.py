from typing import Sequence
from time import time


def count_multiples_of_three_not_five(numbers: Sequence[int]) -> int:
    """
    Return amount of numbers from sequence which are 
    multiples of tree but not multiples of five
    """
    count = 0

    for number in numbers:
        if not number % 3 and number % 5:
            count += 1

    return count


if __name__ == '__main__':
    start = time()
    print(count_multiples_of_three_not_five(range(100)))
    print(time() - start)
