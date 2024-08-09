def get_ramanujan_number(a: int, b: int) -> int:
    """
    Given 'a' and 'b', returns the Ramanujan number
    that is, a**3 + b**3

    Input:
    a (int): first number
    b (int): second number

    Output:
    int: Ramanujan number
    """
    return a**3 + b**3

def is_narcissist(a: int) -> bool:
    """
    Given a number 'a', returns True if it is narcissist
    that is, d0**n + ... + dn**n = a, where n is the number 
    of digits and d0 to dn are its digits

    Input:
    a (int): number to test

    Output:
    bool: True if a is narcissist, False otherwise
    """
    a_str =  str(a)
    n = len(a_str)
    total = sum([int(d)**n for d in a_str])

    return True if total == a else False

def is_palindrome(a: int) -> bool:
    """
    Given a number 'a', returns True if it is palindrome
    that is, it is the same number if you read it from left to right

    Input:
    a (int): number to test

    Output:
    bool: True if a is palindrome, False otherwise
    """
    a_forward = str(a)
    a_backward = a_forward[::-1]

    return True if a_forward == a_backward else False

def is_lychrel(a: int, max_iterations: int=40) -> bool:
    """
    Given a number 'a', returns True if it is Lychrel
    that is, the digit inversion of a plus a is not a palindrome,
    even in an iterative procedure

    Input:
    a (int): number to test
    max_iterations (int): maximum number of iterations, optional, default is 40

    Output:
    bool: True if a is Lychrel, False otherwise
    """
    for iter in range(max_iterations):

        if is_palindrome(a):
            return False

        a += int(str(a)[::-1])

    return True

    