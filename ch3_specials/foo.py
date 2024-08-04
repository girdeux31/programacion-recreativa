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