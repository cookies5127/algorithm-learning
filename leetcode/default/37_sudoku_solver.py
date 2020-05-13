import copy
from typing import List

'''
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    1. Each of the digits 1-9 must occur exactly once in each row.
    2. Each of the digits 1-9 must occur exactly once in each column.
    3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3
       sub-boxes of the grid.

Empty cells are indicated by the character '.'.
'''

EXAMPLES = [
    (
        [
            ['.', '.', '9', '7', '4', '8', '.', '.', '.'],
            ['7', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '2', '.', '1', '.', '9', '.', '.', '.'],
            ['.', '.', '7', '.', '.', '.', '2', '4', '.'],
            ['.', '6', '4', '.', '1', '.', '5', '9', '.'],
            ['.', '9', '8', '.', '.', '.', '3', '.', '.'],
            ['.', '.', '.', '8', '.', '3', '.', '2', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '2', '7', '5', '9', '.', '.'],
        ],
        []
    ),
    (
        [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ],
    ),
]


class Solution:
    def get_pos_values(self, board: List[List[str]], i: int, j: int):
        k = int(i / 3)
        p = int(j / 3)
        inner = [
            board[x][y]
            for x in range(k*3, k*3+3)
            for y in range(p*3, p*3+3)
        ]
        hori = [board[l][j] for l in range(0, 9)]
        vertical = copy.deepcopy(board[i])
        return {
            'inner': inner,
            'hori': hori,
            'vertical': vertical,
        }

    def get_valid_value(self, board: List[List[str]], i: int, j: int) -> List[str]:
        pos_values = self.get_pos_values(board, i, j)

        values = set([
            v
            for value in pos_values.values()
            for v in value
            if v.isdigit()
        ])
        return [
            v
            for v in ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            if v not in values
        ]

    def next_value(self, board: List[List[str]], i: int, j: int) -> bool:
        flag = True

        if j == 8:
            i += 1
            j = 0
        else:
            j += 1

        if i == 9:
            return flag

        v = board[i][j]
        if v.isdigit():
            flag = self.next_value(board, i, j)
        else:
            values = self.get_valid_value(board, i, j)
            if len(values) == 0:
                flag = False
            else:
                k = 0
                while k < len(values):
                    board[i][j] = values[k]
                    flag = self.next_value(board, i, j)
                    if flag:
                        break
                    k += 1

                if k == len(values):
                    flag = False
                    board[i][j] = '.'

        return flag

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.next_value(board, 0, -1)
