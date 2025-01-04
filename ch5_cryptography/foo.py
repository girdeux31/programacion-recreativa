import string
import math

from typing import Optional


def cesar_encode(msg: str, shift: int) -> str:
    """
    Encripts a message by applying a delta in the alphabetical order
    It accepts lower, upper and numbers, symbols are not encoded

    Input:
    msg (str): message to encript
    shift (int): number of letters to shift, use negative int to decode

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

def transposition_encode(msg: str, n: Optional[int]=None) -> str:
    """
    Encripts a message by applying transposition encoding (reorder the characters
    reading vertically in a table n*n)
    It accepts all kind of symbols

    Input:
    msg (str): message to encript
    n (int): table side, length of message must be equal or smaller than n*n,
        it is optional, by default n is calculated so the text fits in the smaller possible table

    Output:
    str: encoded message
    """
    if not n:
        n = math.ceil(math.sqrt(len(msg)))

    if n < 2:
        raise ValueError(f'Parameter \'n\' must be >= 2')

    if len(msg) > n**2:
        raise ValueError(f'Length of message must be <= {n**2}')
    
    msg += ' ' * (n**2 - len(msg))
    msg_encoded = ''

    for shift in range(0, n):
        for idx in range(0 + shift, len(msg), n):
            msg_encoded += msg[idx]

    return msg_encoded

def is_only_ones_and_zeroes(code: str):
    """
    True if string contains all 0s or 1s

    Input:
    code (str): string to check

    Output:
    bool: True if code is only 0s and 1s, False otherwise
    """
    return all([c in '01' for c in code])

def xor_encode(msg: str, code: str) -> str:
    """
    Encripts a message with the xor operator and a code
    xor operator is True when both inputs are different, and it is False when both inputs are equal
    Message and code can only contain 1s or 0s

    Input:
    msg (str): message to encript
    code (str): code used to encode and decode

    Output:
    str: encoded message
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

def vigenere_encode(msg: str, key: str, decode: bool=False) -> str:
    """
    Encripts a message by applying a delta in the alphabetical order
    This delta is based on the key word
    It accepts lower, upper and numbers, symbols are not encoded

    Input:
    msg (str): message to encript
    key (str): key word to encode/decode, can contain any character
    decode (bool): decodes message if True

    Output:
    str: encoded/decoded message
    """
    k_idx = 0
    msg_encoded = ''
    sign = -1 if decode else +1
    
    for m in msg:

        k_idx = 0 if k_idx == len(key) else k_idx
        int_encoded = ord(m) + ord(key[k_idx])*sign
        chr_encoded = chr(int_encoded)
        msg_encoded += chr_encoded
        k_idx += 1

    return msg_encoded
