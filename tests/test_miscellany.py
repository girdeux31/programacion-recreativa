import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch4_miscellany.foo import (
    get_consecutive_sums,
    is_inverted_squared,
)


def test_get_consecutive_sums():

    cs_33 = get_consecutive_sums(33)
    assert len(cs_33) == 3
    assert cs_33[0] == [3, 4, 5, 6, 7, 8]
    assert cs_33[1] == [10, 11, 12]
    assert cs_33[2] == [16, 17]

    cs_975 = get_consecutive_sums(975)
    assert len(cs_975) == 11
    assert (cs_975[0][0], cs_975[0][-1]) == (6, 44)
    assert (cs_975[1][0], cs_975[1][-1]) == (18, 47)
    assert (cs_975[2][0], cs_975[2][-1]) == (25, 50)
    assert cs_975[-2] == [324, 325, 326]
    assert cs_975[-1] == [487, 488]

def test_is_inverted_squared():

    assert is_inverted_squared(12)
    assert is_inverted_squared(13)
    assert not is_inverted_squared(14)