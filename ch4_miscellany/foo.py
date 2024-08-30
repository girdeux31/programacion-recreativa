import math
from typing import List


def inverted(a: int) -> int:
    """
    Given a number 'a', returns a number with inverted digits 

    Input:
    a (int): number to test

    Output:
    int: number with inverted digits of 'a'
    """
    return int(str(abs(a))[::-1])

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
    a_2 = a**2
    inv_a_2 = inverted(inverted(a)**2)

    return True if a_2 == inv_a_2 else False

def get_digital_root(a: int) -> int:
    """
    Given a number 'a', returns a its digital root
    that is, sum its digits recursively until a number with only one digit is obtained

    Input:
    a (int): number to test

    Output:
    int: digital root of a
    """
    a_str = str(a)

    while len(a_str) > 1:
        a = sum([int(i) for i in a_str])
        a_str = str(a)

    return a

def is_powered_number(a: int, power: int=4) -> bool:
    """
    Given a number 'a', returns True if it is a powered number
    that is, the sum of its digits to certain power gives the original number

    Input:
    a (int): number to test
    power (int): power, optional, default is 4

    Output:
    bool: True if a is a powered number, False otherwise
    """
    b = sum([int(i)**power for i in str(a)])

    return True if a == b else False

def get_collatz_reduction(a: int, max_iterations: int=10**4) -> List[int]:
    """
    Given a number 'a', returns its Collatz reduction
    that is, n/2 if a is even else 3n+1, recursively

    Input:
    a (int): number to test
    max_iterations (int): maximum number of iterations, optional, default is 10**4

    Output:
    List[int]: iterations of Collatz conjecture
    """
    numbers = []
    iteration = 0

    while a != 1:
        
        iteration += 1
        a = a/2 if a % 2 == 0 else 3*a+1
        numbers.append(a)

        if iteration > max_iterations:
            break

    return numbers
