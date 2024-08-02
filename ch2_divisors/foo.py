import math

from typing import List


def is_divisor(b: int, a: int) -> bool:
    """
    Given 'a' and 'b', returns True if b is divisor of a
    that is, the remainder of a/b is 0

    Input:
    a (int): number to test in the numerator
    b (int): number to test in the denominator

    Output:
    bool: True if if b is divisor of a, False otherwise
    """
    if a == 0 or b == 0:
        raise ValueError('Parameters \'a\' and \'b\' must not be 0')

    return not a % b

def get_all_divisors(a: int) -> List[int]:
    """
    Given a number 'a', returns all its divisors

    Input:
    a (int): number to test

    Output:
    List(int): list of divisors of a
    """
    b_max = math.ceil(a/2)
    output = [b for b in range(1, b_max+1) if is_divisor(b, a)]

    return output

def are_friends(a: int, b: int) -> bool:
    """
    Given 'a' and 'b', returns True if a and b are friends
    that is, divisors of a sums b and divisors of b sums a

    Input:
    a (int): number to test
    b (int): number to test

    Output:
    bool: True if a and b are friends, False otherwise
    """
    a_divisors = get_all_divisors(a)
    b_divisors = get_all_divisors(b)

    return True if sum(a_divisors) == b and sum(b_divisors) == a else False

def is_perfect(a: int) -> bool:
    """
    Given a number 'a', returns True if it is perfect
    that is, its divisors sum a

    Input:
    a (int): number to test

    Output:
    bool: True if a is perfect, False otherwise
    """
    a_divisors = get_all_divisors(a)

    return True if sum(a_divisors) == a else False

def is_abundant(a: int) -> bool:
    """
    Given a number 'a', returns True if it is abundant
    that is, its divisors sum more than a

    Input:
    a (int): number to test

    Output:
    bool: True if a is abundant, False otherwise
    """
    a_divisors = get_all_divisors(a)

    return True if sum(a_divisors) > a else False

def is_deficient(a: int) -> bool:
    """
    Given a number 'a', returns True if it is deficient
    that is, its divisors sum less than a

    Input:
    a (int): number to test

    Output:
    bool: True if a is deficient, False otherwise
    """
    a_divisors = get_all_divisors(a)

    return True if sum(a_divisors) < a else False

def are_congruents(a: int, b: int, m: int) -> bool:
    """
    Given 'a', 'b' and 'm' returns True if a and b are congruent
    that is, modulus (reminder) of a/m and b/m are the same

    Input:
    a (int): number to test
    b (int): number to test
    m (int): modulus

    Output:
    bool: True if a and b are congruent, False otherwise
    """
    if m <= 0:
        raise ValueError('Parameter m must be bigger than zero')

    return True if a%m == b%m else False
