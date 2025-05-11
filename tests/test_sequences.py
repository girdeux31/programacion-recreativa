import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch6_sequences.foo import (
    humming_seq,
    padovan_seq,
    primorial,
)


def test_humming_seq():

    assert humming_seq(6) == 6
    assert humming_seq(10) == 12
    assert humming_seq(100) == 1536
    assert humming_seq(8, primes=[13, 19, 100]) == 1300

def test_padovan_seq():

    assert padovan_seq(6) == 3
    assert padovan_seq(10) == 9
    assert padovan_seq(50) == 696081

def test_primorial():

    assert primorial(3) == 6
    assert primorial(10) == 210
    assert primorial(20) == 9699690