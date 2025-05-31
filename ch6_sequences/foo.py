import math
import heapq
import itertools


# From chapter 1
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

def humming_seq(n: int, primes: list[int]=[2, 3, 5]) -> list[int]:
    """
    Given 'n', returns the Humming sequence up to the nth element for these primes
    For primes 2, 3 and 5, the sequence contains the product of powers of 2, 3, and 5

    For example: H(2,3,5) = 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, …

    Check out the first 1500 numbers of the Humming sequence H(2,3,5)
    https://rcbj.net/2007/01/30/the-first-1500-hamming-numbers

    Input:
    n (int): sequence limit
    primes list[int]: primes for the Humming sequence

    Output:
    list[int]: sequence
    """
    if n < 1:
        raise ValueError('Parameter \'n\' must be a positive integer')
    
    sequence = []
    seen = set()
    heap = [1]
    
    for _ in range(n):
        val = heapq.heappop(heap)
        sequence.append(val)
        
        for factor in primes:
            next_val = val * factor
            if next_val not in seen:
                seen.add(next_val)
                heapq.heappush(heap, next_val)
    
    return sequence

def padovan_seq(n: int) -> list[int]:
    """
    Given 'n', returns the nth number of the Padovan sequence

    P0 = P1 = P2 = 1
    Pn = P(n-2) + P(n-3)

    Input:
    n (int): sequence limit

    Output:
    list[int]: sequence
    """
    if n < 1:
        raise ValueError('Parameter \'n\' must be a positive integer')
    
    sequence = [1] * 3

    for _ in range(3, n):

        value = sequence[-2] + sequence[-3]
        sequence.append(value)

    return sequence

def primorial(n: int) -> int:
    """
    Given 'n', returns the primorial of n, that is the product of all primes lower or equal than n

    Input:
    n (int): primorial to compute

    Output:
    int
    """
    output = math.prod([p for p in range(2, n+1) if is_prime(p)])
    return output

def primorial_seq(n: int) -> list[int]:
    """
    Given 'n', returns the primorial sequence up to the nth element

    Input:
    n (int): sequence limit

    Output:
    list[int]: sequence
    """
    if n < 1:
        raise ValueError('Parameter \'n\' must be a positive integer')
    
    sequence = [primorial(a) for a in range(1, n+1)]
    return sequence

def is_harshad(n: int) -> bool:
    """
    Given 'n', returns True if n is a harshad number, that is n is divisible by the sum of its digits

    Input:
    n (int): number to check

    Output:
    bool: True if n is a harshad number, False otherwise
    """
    d_sum = sum([int(d) for d in str(n)])
    return True if n % d_sum == 0 else False

def harshad_seq(n: int) -> list[int]:
    """
    Given 'n', returns the Harshad sequence up to the nth element (in base 10)

    Input:
    n (int): sequence limit

    Output:
    list[int]: sequence
    """
    if n < 1:
        raise ValueError('Parameter \'n\' must be a positive integer')
    
    a = 0
    sequence = []

    while len(sequence) < n:
        
        a += 1
        if is_harshad(a):
            sequence.append(a)

    return sequence

def is_absolute_prime(n: int) -> bool:
    """
    Given 'n', returns True if n is an absolute prime number, that is all 
    permutations of the digits of n are primes

    Input:
    n (int): number to check

    Output:
    bool: True if n is an absolute prime, False otherwise
    """
    digits = [d for d in str(n)]
    permutations = itertools.permutations(digits, len(digits))
        
    return all(
        [
            is_prime(int(''.join(permutation)))
            for permutation in permutations
        ]
    )

def absolute_prime_seq(n: int) -> list[int]:
    """
    Given 'n', returns the absolute prime sequence up to the nth element

    Input:
    n (int): sequence limit

    Output:
    list[int]: sequence
    """
    if n < 1:
        raise ValueError('Parameter \'n\' must be a positive integer')
    
    a = 0
    sequence = []

    while len(sequence) < n:
        
        a += 1
        if is_absolute_prime(a):
            sequence.append(a)

    return sequence