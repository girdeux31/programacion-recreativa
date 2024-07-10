import math


def is_prime(n):
    """
    Given a number 'n', returns True if it is prime

    Input:
    n (int): number to test

    Output:
    bool: True if n is prime, False otherwise
    """
    if not isinstance(n, int):
        raise ValueError(f'Number \'n\' must be an integer bigger than one')

    if n < 2:
        return False
        
    upper_limit = math.ceil(math.sqrt(n))
    remainders = [n % i for i in range(2, upper_limit)]

    return all(remainders)

def are_twin_primes(p, q):
    """
    Given the numbers p and q, return True if both are twin primes,
    that is, both are primes and are separated by two units (q = p+2)

    Input:
    p (int): first number to test
    q (int): second number to test

    Output:
    bool: True if p and q are twin primes, False otherwise
    """
    if is_prime(p) and is_prime(q) \
        and (p == q+2 or q == p+2):
        return True

    return False
