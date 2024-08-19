import math


def get_consecutive_sums(a: int) -> list:
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