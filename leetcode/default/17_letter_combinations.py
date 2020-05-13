from typing import List


'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like telephone buttons) is given below.
Note that 1 dose not map to any letters.

Example:

    Input: '23'
    Ouput: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
'''

EXAMPLES = [
    (
        '23',
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'],
    )
]


class Solution:
    def get_letters(self, arrays: List[str], strings: str) -> List[str]:
        if not arrays:
            arrays = ['']
        return [
            array + str
            for str in strings
            for array in arrays
        ]

    def letterCombinations(self, digits: str) -> List[str]:
        LETTER_MAP = {
            '1': '*',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' ',
        }

        arrays = []

        for digit in digits:
            arrays = self.get_letters(arrays, LETTER_MAP[digit])

        return arrays
