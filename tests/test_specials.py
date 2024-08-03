import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch3_specials.foo import (
    get_ramanujan_number,
)


def test_get_ramanujan_number():

    assert get_ramanujan_number(1, 12) == 1729
    assert get_ramanujan_number(9, 10) == 1729