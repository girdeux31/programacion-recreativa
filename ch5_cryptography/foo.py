import string
import math


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

def transposition_encode(msg: str, n: int=None) -> str:
    """
    Encripts a message by applying transposition encoding (reorder the characters
    reading vertically in a table n*n)
    It accepts kind of symbols

    Input:
    msg (str): message to encript
    n (int): table side, length of message must be equal or smaller than n*n,
        it is optional, by default i calculates n so the text fits in the smaller possible table

    Output:
    str: encoded message
    """
    if not n:
        n = math.ceil(math.sqrt(msg))
    if len(msg) > n**2:
        raise ValueError(f'Length of message must be <= {n**2}')
    
    msg += ' ' * (n**2 - len(msg))
    msg_encoded = ''

    for shift in range(0, n):
        for idx in range(0 + shift, len(msg), n):
            msg_encoded += msg[idx]

    return msg_encoded