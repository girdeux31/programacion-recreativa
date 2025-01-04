import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch5_cryptography.foo import (
    cesar_encode,
    transposition_encode,
    is_only_ones_and_zeroes,
    xor_encode,
    vigenere_encode,
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

    assert transposition_encode('Esto es un secreto') == 'Ee e ssst t eo ouc   nr  '
    assert transposition_encode('Esto es un secreto', 5) == 'Ee e ssst t eo ouc   nr  '
    assert transposition_encode('Esto es un secreto muy guardado!', 6) == 'Ese uos cma!turur oneyd   t a esogd '
    assert transposition_encode('Ese uos cma!turur oneyd   t a esogd ', 6) == 'Esto es un secreto muy guardado!    '

def test_is_only_ones_and_zeroes():

    assert is_only_ones_and_zeroes('1')
    assert is_only_ones_and_zeroes('0')
    assert is_only_ones_and_zeroes('11010101011111000111')
    assert not is_only_ones_and_zeroes('11010101011111000121')

def test_xor_encode():

    assert xor_encode('100100', '0011') == '101000'
    assert xor_encode('101000', '0011') == '100100'

def test_vigenere_encode():
    
    key = 'hack! $'
    assert vigenere_encode('Th1s 1s V1g3n3r3 c0d3!_9', key) == '¼É\x94ÞAQ\x97\x88·\x94ÒT\x8eWÚ\x94\x83ÎQ\x84W\x89À\x9c'
    assert vigenere_encode('¼É\x94ÞAQ\x97\x88·\x94ÒT\x8eWÚ\x94\x83ÎQ\x84W\x89À\x9c', key, decode=True) == 'Th1s 1s V1g3n3r3 c0d3!_9'