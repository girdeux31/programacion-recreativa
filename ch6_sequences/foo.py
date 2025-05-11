import heapq


def humming_seq(n: int, primes: list[int]=[2, 3, 5]) -> list[int]:
    """
    Given 'n', returns the nth number of the Humming sequence for these primes
    Hn(primes), that is the nth integers whose only divisors are the primes listed

    For example: H(2,3,5) = 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, …
    so H5(2, 3, 5) = 6

    Check out the first 1500 numbers of the Humming sequence H(2,3,5)
    https://rcbj.net/2007/01/30/the-first-1500-hamming-numbers

    Input:
    n (int): elements in the sequence
    primes list[int]: primes for the Humming sequence

    Output:
    list[int]: sequence
    """
    if n < 1:
        raise ValueError('Parameter \'n\' must be a positive integer')
    
    hamming = []
    seen = set()
    heap = [1]
    
    for _ in range(n):
        val = heapq.heappop(heap)
        hamming.append(val)
        
        for factor in primes:
            next_val = val * factor
            if next_val not in seen:
                seen.add(next_val)
                heapq.heappush(heap, next_val)
    
    return hamming[-1]