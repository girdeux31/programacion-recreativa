import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch5_cryptography.foo import (
    cesar_encode,
    transposition_encode,
)


def test_cesar_encode():

    assert cesar_encode('ABCXYZ', 1) == 'BCDYZA'
    assert cesar_encode('ABCXYZ', 26) == 'ABCXYZ'
    assert cesar_encode('abcxyz', 1) == 'bcdyza'
    assert cesar_encode('abcxyz', 26) == 'abcxyz'
    assert cesar_encode('aBcXyZ', 1) == 'bCdYzA'
    assert cesar_encode('012789', 1) == '123890'
    assert cesar_encode('Th1s 1s Cesar c0d3!_9', 3) == 'Wk4v 4v Fhvdu f3g6!_2'
    assert cesar_encode('Wk4v 4v Fhvdu f3g6!_2', -3) == 'Th1s 1s Cesar c0d3!_9'

def test_transposition_encode():

    assert transposition_encode('Esto es un secreto', 5) == 'Eest sseo t c  our   ne  '