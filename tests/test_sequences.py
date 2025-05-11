import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch6_sequences.foo import (
    humming_seq,
    padovan_seq,
    primorial,
    primorial_seq,
    is_harshad,
    harshad_seq,
)


def test_humming_seq():

    assert humming_seq(6)[-1] == 6
    assert humming_seq(10)[-1] == 12
    assert humming_seq(100)[-1] == 1536
    assert humming_seq(8, primes=[13, 19, 100])[-1] == 1300
    assert len(humming_seq(100)) == 100

def test_padovan_seq():

    assert padovan_seq(6)[-1] == 3
    assert padovan_seq(10)[-1] == 9
    assert padovan_seq(50)[-1] == 696081
    assert len(padovan_seq(50)) == 50

def test_primorial():

    assert primorial(3) == 6
    assert primorial(10) == 210
    assert primorial(20) == 9699690

def test_primorial_seq():

    assert primorial_seq(3)[-1] == 6
    assert primorial_seq(10)[-1] == 210
    assert primorial_seq(20)[-1] == 9699690
    assert len(primorial_seq(20)) == 20

def test_is_harshad():

    assert is_harshad(12)
    assert is_harshad(18)
    assert is_harshad(84)
    assert is_harshad(1729)
    assert is_harshad(521478)
    assert not is_harshad(19)
    assert not is_harshad(521479)

def test_harshad_seq():

    assert harshad_seq(3)[-1] == 3
    assert harshad_seq(12)[-1] == 18
    assert harshad_seq(20)[-1] == 42
    assert harshad_seq(40)[-1] == 117
