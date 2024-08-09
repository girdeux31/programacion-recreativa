import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch3_specials.foo import (
    get_ramanujan_number,
    is_narcissist,
    is_palindrome,
    is_lychrel,
)


def test_get_ramanujan_number():

    assert get_ramanujan_number(1, 12) == 1729
    assert get_ramanujan_number(9, 10) == 1729

def test_is_narcissist():

    assert is_narcissist(1)
    assert is_narcissist(9)
    assert is_narcissist(153)
    assert is_narcissist(54748)
    assert not is_narcissist(54749)

def test_is_palindrome():

    assert is_palindrome(1)
    assert is_palindrome(121)
    assert is_palindrome(12345654321)
    assert is_palindrome(123456654321)
    assert not is_palindrome(12345665432)

def test_is_lychrel():

    assert not is_lychrel(12)
    assert not is_lychrel(102)
    assert not is_lychrel(201)
    assert not is_lychrel(48)
    assert not is_lychrel(84)
    assert not is_lychrel(187)