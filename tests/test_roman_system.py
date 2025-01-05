import sys

sys.path.append(r'/home/cmesado/Documents/programacion-recreativa')

from ch5_cryptography.roman_system import RomanSystem


def test_split_roman_in_chunks():

    assert RomanSystem._split_roman_in_chunks('I') == ['I']
    assert RomanSystem._split_roman_in_chunks('M') == ['M']
    assert RomanSystem._split_roman_in_chunks('MMM') == ['MMM']
    assert RomanSystem._split_roman_in_chunks('MMMI') == ['MMM', 'I']
    assert RomanSystem._split_roman_in_chunks('MMMIX') == ['MMM', 'IX']
    assert RomanSystem._split_roman_in_chunks('MMMCDXLIX') == ['MMM', 'CD', 'XL', 'IX']

def test_roman_chunk_to_decimal():

    assert RomanSystem._roman_chunk_to_decimal('I') == 1
    assert RomanSystem._roman_chunk_to_decimal('III') == 3
    assert RomanSystem._roman_chunk_to_decimal('IV') == 4
    assert RomanSystem._roman_chunk_to_decimal('CM') == 900
    assert RomanSystem._roman_chunk_to_decimal('MMM') == 3000

def test_roman_to_decimal():

    assert RomanSystem.roman_to_decimal('I') == 1
    assert RomanSystem.roman_to_decimal('III') == 3
    assert RomanSystem.roman_to_decimal('IX') == 9
    assert RomanSystem.roman_to_decimal('LIX') == 59
    assert RomanSystem.roman_to_decimal('CMXLIX') == 949
    assert RomanSystem.roman_to_decimal('MMMCCCLXXX') == 3380 
    assert RomanSystem.roman_to_decimal('MMMCCCIX') == 3309

def test_decimal_to_roman():

    assert RomanSystem.decimal_to_roman(1) == 'I'
    assert RomanSystem.decimal_to_roman(3) == 'III'
    assert RomanSystem.decimal_to_roman(9) == 'IX'
    assert RomanSystem.decimal_to_roman(59) == 'LIX'
    assert RomanSystem.decimal_to_roman(949) == 'CMXLIX'
    assert RomanSystem.decimal_to_roman(3380) == 'MMMCCCLXXX'
    assert RomanSystem.decimal_to_roman(3309) == 'MMMCCCIX'