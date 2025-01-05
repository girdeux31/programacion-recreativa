import string
import math

from typing import Optional

from ch5_cryptography.roman_system import RomanSystem


def cesar_encoder(msg: str, shift: int) -> str:
    """
    Encrypt a message by applying a delta in the alphabetical order
    It accepts lower, upper and numbers, symbols are not encoded

    Input:
    msg (str): message to encrypt
    shift (int): number of letters to shift

    Output:
    str: encoded message
    """
    letter_base = len(string.ascii_lowercase)
    digit_base = len(string.digits)

    def encode_digit(chr: str, shift: int):
        idx_encoded = (int(chr) + shift) % digit_base
        return string.digits[idx_encoded]
    
    def encode_letter(chr: str, shift: int, isupper: bool=False):
        ascii_list = string.ascii_uppercase if isupper else string.ascii_lowercase
        idx = ascii_list.index(chr)
        _, idx_encoded = divmod(idx + shift, letter_base)
        return ascii_list[idx_encoded]
    
    msg_encoded = ''
    
    for chr in msg:
        
        if chr.isdigit():
            chr_encoded = encode_digit(chr, shift)
        elif chr.islower() or chr.isupper():
            chr_encoded = encode_letter(chr, shift, isupper=chr.isupper())
        else:
            chr_encoded = chr

        msg_encoded += chr_encoded

    return msg_encoded

def cesar_decoder(msg: str, shift: int) -> str:
    """
    Decrypts a message encrypted by cesar encoding

    Input:
    msg (str): message to decrypt
    shift (int): must be the same value used in the encoding

    Output:
    str: decoded message
    """
    msg_decoded = cesar_encoder(msg, -shift)

    return msg_decoded

def transposition_encoder(msg: str, n: int) -> str:
    """
    Encrypt a message by applying transposition encoding (reorder the characters
    reading vertically in a table n*n)
    It accepts all kind of symbols

    Input:
    msg (str): message to encrypt
    n (int): table side, length of message must be equal or smaller than n*n

    Output:
    str: encoded message
    """
    min_n = math.ceil(math.sqrt(len(msg)))

    if n < min_n:
        raise ValueError(f'Parameter \'n\' must be equal or bigger than {min_n}')
    
    msg += ' ' * (n**2 - len(msg))
    msg_encoded = ''

    for shift in range(0, n):
        for idx in range(0 + shift, len(msg), n):
            msg_encoded += msg[idx]

    return msg_encoded

def transposition_decoder(msg: str, n: int) -> str:
    """
    Decrypts a message encrypted by transposition encoding

    Input:
    msg (str): message to decrypt
    n (int): must be the same value used in the encoding, mandatory

    Output:
    str: decoded message
    """
    msg_decoded = transposition_encoder(msg, n)

    return msg_decoded

def is_only_ones_and_zeroes(code: str):
    """
    True if string contains all 0s or 1s

    Input:
    code (str): string to check

    Output:
    bool: True if code is only 0s and 1s, False otherwise
    """
    return all([c in '01' for c in code])

def xor_encoder(msg: str, code: str) -> str:
    """
    Encrypt a number with the xor operator and a code
    xor operator is True when both inputs are different, and it is False when both inputs are equal
    Number and code can only contain 1s or 0s

    Input:
    msg (str): number to encrypt
    code (str): code used to encode and decode

    Output:
    str: encoded number
    """
    if not is_only_ones_and_zeroes(msg):
        raise ValueError(f'Message {msg} have other characters than 1s and 0s')

    if not is_only_ones_and_zeroes(code):
        raise ValueError(f'Code {msg} have other characters than 1s and 0s')

    c_idx = 0
    msg_encoded = ''

    for m_idx in range(len(msg)):
        
        m = msg[m_idx]
        c_idx = 0 if c_idx == len(code) else c_idx
        c = code[c_idx]
        c_idx += 1

        msg_encoded += str(int(m) ^ int(c))
    
    return msg_encoded

def xor_decoder(msg: str, code: str) -> str:
    """
    Decrypts a number encrypted by xor encoding

    Input:
    msg (str): number to decrypt
    code (str): must be the same value used in the encoding

    Output:
    str: decoded number
    """
    msg_decoded = xor_encoder(msg, code)

    return msg_decoded

def vigenere_encoder(msg: str, key: str, _decode: Optional[bool]=False) -> str:
    """
    Encrypt a message by applying a delta in the alphabetical order
    This delta is based on the key word
    It accepts lower, upper and numbers, symbols are not encoded

    Input:
    msg (str): message to encrypt
    key (str): key word to encode/decode, can contain any character
    _decode (bool): only internal use

    Output:
    str: encoded/decoded message
    """
    k_idx = 0
    msg_encoded = ''
    sign = -1 if _decode else +1
    
    for m in msg:

        k_idx = 0 if k_idx == len(key) else k_idx
        int_encoded = ord(m) + ord(key[k_idx])*sign
        chr_encoded = chr(int_encoded)
        msg_encoded += chr_encoded
        k_idx += 1

    return msg_encoded

def vigenere_decoder(msg: str, key: str) -> str:
    """
    Decrypts a message encrypted by vigenere encoding

    Input:
    msg (str): message to decrypt
    key (str): must be the same value used in the encoding

    Output:
    str: decoded message
    """
    msg_decoded = vigenere_encoder(msg, key, _decode=True)

    return msg_decoded

def roman_encoder(number: int) -> str:
    """
    Encrypt a number using roman system
    Message only accepts I, V, X, L, C, D, M

    Input:
    number (int): decimal number to encrypt

    Output:
    str: encoded roman number
    """
    msg_encoded = RomanSystem.decimal_to_roman(number)

    return msg_encoded

def roman_decoder(number: str) -> int:
    """
    Decrypts a number encrypted by roman encoding

    Input:
    number (str): roman number to decrypt

    Output:
    int: decoded decimal number
    """
    msg_decoded = RomanSystem.roman_to_decimal(number)

    return msg_decoded
