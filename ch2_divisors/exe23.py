import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from foo import is_perfect
from ch1_primes.foo import is_prime


def bin2dec(b: str):
    """Binary to decimal convertor"""
    
    return int(b, 2)


print('Exercise 2.3')

max_digits = 64
n_ones = 0

print(f'{"prime":10} {"binary":{max_digits}} {"decimal":20}')
print('='*10 + ' ' + '='*max_digits + ' ' + '='*20)

while True:

    n_ones += 1

    if not is_prime(n_ones):
        continue

    n_zeros = n_ones - 1
    binary = '1'*n_ones + '0'*n_zeros

    if len(binary) > max_digits:
        break

    decimal = bin2dec(binary)

    print(f'{n_ones:10} {binary:{max_digits}} {decimal:20}')
