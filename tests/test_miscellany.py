import sys
import numpy as np

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch4_miscellany.foo import (
    inverted,
    get_consecutive_sums,
    is_inverted_squared,
    get_digital_root,
    is_powered_number,
    get_collatz_reduction,
    ethiopian_multiplication,
    check_eulers_conjecture,
)


def test_inverted():

    assert inverted(123) == 321
    assert inverted(10) == 1
    assert inverted(1) == 1
    
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

def test_get_digital_root():

    assert get_digital_root(297) == 9
    assert get_digital_root(10) == 1
    assert get_digital_root(1) == 1

def test_is_powered_number():

    assert is_powered_number(1634)
    assert not is_powered_number(1635)

def test_get_collatz_reduction():

    assert len(get_collatz_reduction(921)) == 129
    assert get_collatz_reduction(921)[10] == 584

def test_ethiopian_multiplication():

    assert ethiopian_multiplication(21, 42) == 882
    assert ethiopian_multiplication(42, 21) == 882
    assert ethiopian_multiplication(456582, 874354) == 399214298028
    assert ethiopian_multiplication(456589, 874353) == 399219961917
    assert ethiopian_multiplication(1, 20) == 20
    assert ethiopian_multiplication(1, 15) == 15
    assert ethiopian_multiplication(1, 1) == 1
    assert ethiopian_multiplication(0, 1) == 0
    assert ethiopian_multiplication(1, 0) == 0
    assert ethiopian_multiplication(0, 0) == 0

def test_check_eulers_conjecture():

    assert check_eulers_conjecture(np.array([3, 4, 5]), 2)
    assert check_eulers_conjecture(np.array([3, 4, 5, 6]), 3)
    assert check_eulers_conjecture(np.array([95800, 217519, 414560, 422481]), 4)
    assert check_eulers_conjecture(np.array([27, 84, 110, 133, 144]), 5)
    assert check_eulers_conjecture(np.array([-220, 5027, 6237, 14068, 14132]), 5)
    assert check_eulers_conjecture(np.array([55, 3183, 28969, 85282, 85359]), 5)
    assert check_eulers_conjecture(np.array([90, 223, 478, 524, 748, 1088, 1190, 1324, 1409]), 8)