import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch5_cryptography.foo import (
    cesar_encoder,
    cesar_decoder,
    transposition_encoder,
    transposition_decoder,
    is_only_ones_and_zeroes,
    xor_encoder,
    xor_decoder,
    vigenere_encoder,
    vigenere_decoder,
    roman_encoder,
    roman_decoder,
)


def test_cesar_encoder():

    assert cesar_encoder('ABCXYZ', 1) == 'BCDYZA'
    assert cesar_encoder('ABCXYZ', 26) == 'ABCXYZ'
    assert cesar_encoder('abcxyz', 1) == 'bcdyza'
    assert cesar_encoder('abcxyz', 26) == 'abcxyz'
    assert cesar_encoder('aBcXyZ', 1) == 'bCdYzA'
    assert cesar_encoder('012789', 1) == '123890'
    assert cesar_encoder('Th1s 1s Cesar c0d3!_9', 3) == 'Wk4v 4v Fhvdu f3g6!_2'

def test_cesar_decoder():

    assert cesar_decoder('Wk4v 4v Fhvdu f3g6!_2', 3) == 'Th1s 1s Cesar c0d3!_9'

def test_transposition_encoder():

    assert transposition_encoder('Esto es un secreto', 5) == 'Ee e ssst t eo ouc   nr  '
    assert transposition_encoder('Esto es un secreto muy guardado!', 6) == 'Ese uos cma!turur oneyd   t a esogd '

def test_transposition_decoder():

    assert transposition_decoder('Ese uos cma!turur oneyd   t a esogd ', 6) == 'Esto es un secreto muy guardado!    '

def test_is_only_ones_and_zeroes():

    assert is_only_ones_and_zeroes('1')
    assert is_only_ones_and_zeroes('0')
    assert is_only_ones_and_zeroes('11010101011111000111')
    assert not is_only_ones_and_zeroes('11010101011111000121')

def test_xor_encoder():

    assert xor_encoder('100100', '0011') == '101000'

def test_xor_decoder():

    assert xor_decoder('101000', '0011') == '100100'

def test_vigenere_encoder():
    
    key = 'hack! $'
    assert vigenere_encoder('Th1s 1s V1g3n3r3 c0d3!_9', key) == '¼É\x94ÞAQ\x97\x88·\x94ÒT\x8eWÚ\x94\x83ÎQ\x84W\x89À\x9c'

def test_vigenere_decoder():

    key = 'hack! $'
    assert vigenere_decoder('¼É\x94ÞAQ\x97\x88·\x94ÒT\x8eWÚ\x94\x83ÎQ\x84W\x89À\x9c', key) == 'Th1s 1s V1g3n3r3 c0d3!_9'

def test_roman_encoder():

    assert roman_encoder(3358) == 'MMMCCCLVIII'
    assert roman_encoder(949) == 'CMXLIX'

def test_roman_decoder():

    assert roman_decoder('MMMCCCLVIII') == 3358
    assert roman_decoder('CMXLIX') == 949
