import math

from typing import List, Tuple


def is_prime(n: int) -> bool:
    """
    Given a number 'n', returns True if it is prime

    Input:
    n (int): number to test

    Output:
    bool: True if n is prime, False otherwise
    """
    if not isinstance(n, int):
        raise ValueError(f'Number \'n\' must be an integer')

    if n < 2:
        return False

    if n == 2:
        return True
        
    upper_limit = math.ceil(math.sqrt(n))
    remainders = [n % i for i in range(2, upper_limit+1)]

    return all(remainders)

def are_twin_primes(p: int, q: int) -> bool:
    """
    Given the numbers 'p' and 'q', return True if both are twin primes,
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

def get_marsenne_number(n: int) -> int:
    """
    Computes marsenne number M(n) = 2**n-1

    Input:
    n (int): argument to marsenne function

    Output:
    int: marsenne number of n
    """
    if not isinstance(n, int) or n < 2:
        raise ValueError(f'Number \'n\' must be an integer bigger than one')

    return 2**n - 1

def is_marsenne_prime(n: int) -> bool:
    """
    Given a number 'n', returns True if it is prime and its marsenne number is also prime

    Input:
    n (int): number to test

    Output:
    bool: True if n is marsenne prime, False otherwise
    """
    if is_prime(n) and is_prime(get_marsenne_number(n)):
        return True
    
    return False

def is_sophie_prime(n: int) -> bool:
    """
    Given a number 'n', returns True if it is prime and its 
    sophie number (2*n+1) is also prime

    Input:
    n (int): number to test

    Output:
    bool: True if n is sophie prime, False otherwise
    """
    m = 2*n + 1

    if is_prime(n) and is_prime(m):
        return True
    
    return False

def get_cunningham_chain(n: int, nmax: int=10**6, kind: int=1) -> List[int]:
    """
    Given a number 'n', returns the cunningham chain, where 
    n(i+1) = 2*n(i) + 1 if first kind, and
    n(i+1) = 2*n(i) - 1 if second kind

    Input:
    n (int): number to start the chain
    nmax (int): maximum chanin number, optional, by default 10**6
    kind (1): chain kind, optional, by default 1, options are 1 or 2

    Output:
    List[int]: chain members
    """
    if kind != 1 and kind != 2:
        raise ValueError(f'Chain kind must be \'1\' or \'2\'')
    
    output = []
    m = 1 if kind==1 else -1

    while is_prime(n):

        output.append(n)
        n = 2*n + m

        if n > nmax:
            break
    
    return output

def get_goldbach_combinations(n: int) -> List[Tuple[int]]:
    """
    Given a number 'n', returns all goldbach combinations for that number 
    n = p + q, where p and q are prime numbers

    Input:
    n (int): number to test

    Output:
    List[Tuple[int]]: goldbach posibilities
    """
    if n % 2 and n <= 2:
        raise ValueError(f'n must be even and bigger than 2')
    
    output = []
    nmax = math.ceil(n/2)  # TODO

    for p in range(2, n):
        for q in range(2, n):
            if is_prime(p) and is_prime(q) \
                and p+q == n and (q, p) not in output:
                output.append((p, q))

    return output
