import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch1_primes.foo import (
    is_prime,
    are_twin_primes,
    get_marsenne_number,
    is_marsenne_prime,
    is_sophie_prime,
    get_cunningham_chain,
    get_goldbach_combinations,
)


def test_is_prime():

    assert not is_prime(-3)
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)
    assert is_prime(11)
    assert is_prime(17)
    assert is_prime(19)
    assert is_prime(36444293)
    assert not is_prime(36444294)

def test_are_twin_primes():

    assert are_twin_primes(3, 5)
    assert are_twin_primes(5, 7)
    assert not are_twin_primes(9, 13)
    assert not are_twin_primes(10, 12)

def test_marsenne():

    assert get_marsenne_number(2) == 3
    assert get_marsenne_number(4) == 15
    assert get_marsenne_number(7) == 127

def test_is_marsenne_prime():

    assert is_marsenne_prime(2)
    assert not is_marsenne_prime(4)
    assert not is_marsenne_prime(6)
    assert is_marsenne_prime(7)

def test_is_sophie_prime():

    assert is_sophie_prime(2)
    assert not is_sophie_prime(47)

def test_get_cunningham_chain():
    
    assert get_cunningham_chain(2) == [2, 5, 11, 23, 47]
    assert get_cunningham_chain(89) == [89, 179, 359, 719, 1439, 2879]
    assert get_cunningham_chain(100) == []

def test_get_goldbach_combinations():

    assert len(get_goldbach_combinations(14)) == 2
    assert len(get_goldbach_combinations(222)) == 11