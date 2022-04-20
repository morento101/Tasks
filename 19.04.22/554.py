from typing import List
from time import time


def pythagorean_triples(n: int) -> List[tuple]:
    """
    Returns list of tuples with all pythagorean triples triples which satisfy
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
    print(pythagorean_triples(50))
    print(time() - start)
