import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch2_divisors.foo import (
    is_divisor,
    get_all_divisors,
    are_friends,
    is_perfect,
    is_abundant,
    is_deficient,
    are_congruents,
)


def test_is_multiple():

    assert is_divisor(2, 2)
    assert is_divisor(1, 4)
    assert is_divisor(-1, 4)
    assert is_divisor(1, -4)
    assert is_divisor(-1, -4)
    assert is_divisor(2, 4)
    assert is_divisor(3, 9)
    assert is_divisor(128, 256)
    assert not is_divisor(3, 4)
    assert not is_divisor(2, 59)
    assert not is_divisor(13, 654)

def test_get_all_divisors():

    assert get_all_divisors(0) == []
    assert get_all_divisors(2) == [1]
    assert get_all_divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    assert get_all_divisors(284) == [1, 2, 4, 71, 142]

def test_are_friends():

    assert are_friends(220, 284)
    assert are_friends(284, 220)
    assert are_friends(1184, 1210)
    assert are_friends(6232, 6368)
    assert are_friends(17296, 18416)
    assert are_friends(9363584, 9437056)
    assert not are_friends(220+1, 284)

def test_is_perfect():

    assert is_perfect(6)
    assert is_perfect(28)
    assert is_perfect(496)
    assert not is_perfect(497)

def test_is_abundant():

    assert is_abundant(12)
    assert not is_abundant(10)
    assert not is_abundant(6)

def test_is_deficient():

    assert not is_deficient(12)
    assert is_deficient(10)
    assert not is_deficient(6)

def test_are_congruents():

    assert are_congruents(13, 21, 4)
    assert not are_congruents(13, 21, 3)