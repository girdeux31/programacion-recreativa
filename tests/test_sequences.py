import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch6_sequences.foo import (
    humming_seq
)


def test_humming_seq():

    assert humming_seq(6) == 6
    assert humming_seq(10) == 12
    assert humming_seq(100) == 1536
    assert humming_seq(8, primes=[13, 19, 100]) == 1300
