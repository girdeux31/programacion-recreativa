import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from primes.foo import is_prime, are_twin_primes


def test_is_prime():

    assert not is_prime(-3)
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(11)
    assert is_prime(36444293)
    assert not is_prime(36444294)

def test_are_twin_primes():

    assert are_twin_primes(3, 5)
    assert are_twin_primes(5, 7)
    assert not are_twin_primes(9, 13)
    assert not are_twin_primes(10, 12)