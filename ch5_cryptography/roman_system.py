from typing import List

ROMAN_TO_DECIMAL = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
ROMAN_MAGNITUDES = {
    1: {'x1': 'I', 'x5': 'V', 'x10': 'X'},
    10: {'x1': 'X', 'x5': 'L', 'x10': 'C'},
    100: {'x1': 'C', 'x5': 'D', 'x10': 'M'},
    1000: {'x1': 'M'}
}
ROMAN_RULES = {
    1: ['x1'],
    2: ['x1', 'x1'],
    3: ['x1', 'x1', 'x1'],
    4: ['x1', 'x5'],
    5: ['x5'],
    6: ['x5', 'x1'],
    7: ['x5', 'x1', 'x1'],
    8: ['x5', 'x1', 'x1', 'x1'],
    9: ['x1', 'x10'],
    10: ['x10'],
}


class RomanSystem:

    def _is_roman_number(roman: str) -> bool:

        for r in roman:
            if r not in ROMAN_TO_DECIMAL.keys():
                return False

        return True

    @staticmethod
    def _split_roman_in_chunks(roman: str) -> List[str]:

        chunks = []
        i_start = 0

        while i_start <= len(roman)-1:

            chunk = ''
            for i in range(i_start, len(roman)):

                current_decimal = ROMAN_TO_DECIMAL[roman[i]]
                next_decimal = ROMAN_TO_DECIMAL[roman[i+1]] if i+1 < len(roman) else None
                chunk += roman[i]
                i_start += 1

                if next_decimal and next_decimal < current_decimal:
                    break

            chunks.append(chunk)

        return chunks

    @staticmethod
    def _roman_chunk_to_decimal(chunk: str) -> int:

        decimal = 0

        for i in range(len(chunk)):

            current_decimal = ROMAN_TO_DECIMAL[chunk[i]]
            next_decimal = ROMAN_TO_DECIMAL[chunk[i+1]] if i+1 < len(chunk) else None
            sign = +1

            if next_decimal and current_decimal != next_decimal:
                sign = -1

            decimal += sign*current_decimal

        return decimal

    @classmethod
    def roman_to_decimal(cls, roman: str) -> int:

        if not cls._is_roman_number(roman):
            raise ValueError(f'Number \'{roman}\' does not appear to be a roman number')

        chunks = cls._split_roman_in_chunks(roman)
        decimal = sum(cls._roman_chunk_to_decimal(chunk) for chunk in chunks)

        return decimal

    @staticmethod
    def _decimal_to_roman_chunk(digit: int, magnitude: int):

        chunk = ''

        if digit > 0:
            for key in ROMAN_RULES[digit]:
                chunk += ROMAN_MAGNITUDES[magnitude][key]

        return chunk

    @classmethod
    def decimal_to_roman(cls, decimal: int) -> str:

        roman = ''
        decimal = str(decimal)
        digits = [int(d) for d in decimal]
        magnitudes = [10**m for m in range(len(decimal))]
        magnitudes.reverse()

        for digit, magnitude in zip(digits, magnitudes):
            roman += cls._decimal_to_roman_chunk(digit, magnitude)

        return roman
