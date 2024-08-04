import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch3_specials.foo import (
    get_ramanujan_number,
    is_narcissist,
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