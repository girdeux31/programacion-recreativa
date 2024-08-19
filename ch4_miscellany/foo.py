import math
from typing import List


def get_consecutive_sums(a: int) -> List[List[int]]:
    """
    Given a number 'a', returns a list of its consecutive sums
    that is, b0+...+bn = a, where bi = b(i-1) +1

    Input:
    a (int): number to test

    Output:
    list: list of consecutive sums of a
    """
    output = []
    max_b = math.ceil(a/2)

    for b0 in range(max_b):
        total = 0
        for bi in range(b0, max_b+1):
            total += bi
            if total > a:
                break
            if total == a:
                output.append(list(range(b0, bi+1)))
                break

    return output

def is_inverted_squared(a: int) -> list:
    """
    Given a number 'a', returns True if it is an inverted squared
    that is, a**2 == a[::-1]**2

    Input:
    a (int): number to test

    Output:
    bool: True if a is an inverted squared, False otherwise
    """

    def inverted(a: int) -> int:
        """
        Given a number 'a', returns a number with inverted digits 

        Input:
        a (int): number to test

        Output:
        int: number with inverted digits of 'a'
        """
        return int(str(a)[::-1])

    a_2 = a**2
    inv_a_2 = inverted(inverted(a)**2)

    return True if a_2 == inv_a_2 else False