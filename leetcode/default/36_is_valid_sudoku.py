'''
36. Valid Sudoku

Detemine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:

    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without
       repetition.

The Sudoku board could be partially filled, where empty cells are filled with the
character '.'.

Example 1:

    Input:
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
    ]
    Ouput: true

Example 2:

    Input:
    [
      ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
      ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
      ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
      ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
      ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
      ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
      ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
      ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
      ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner
    being modified to 8. Since there are two 8's in the top left 3x3 sub-box,
    it is invalid.

Note:

    * A Sudouk board (partially filled) could be valid but is not necessarily solvable
    * Only the filled cells need to be validated according to the mentioned rules.
    * The given board contain only digits 1-9 and the character '.'.
    * The given board size is always 9x9.
'''

EXAMPLES = [
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
        ], True,
    ),
    (
        [
            ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ], False,
    ),
]


class Solution:
    def check_value(self, v: str, arr: List[str]) -> bool:
        arr.remove(v)
        return v not in arr

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True

        i = 0
        while i < 9:
            j = 0
            while j < 9:
                v = board[i][j]
                if v.isdigit():
                    k = int(i / 3)
                    p = int(j / 3)

                    inner = [
                        board[x][y]
                        for x in range(k*3, k*3+3)
                        for y in range(p*3, p*3+3)
                    ]
                    hori = [board[l][j] for l in range(0, 9)]
                    vertical = copy.deepcopy(board[i])

                    for arr in [inner, hori, vertical]:
                        flag = self.check_value(v, arr)
                        if not flag:
                            break

                j = j + 1 if flag else 9

            i = i + 1 if flag else 9

        return flag
