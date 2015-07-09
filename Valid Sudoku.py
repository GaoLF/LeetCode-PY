#coding=utf-8
class Solution:
    # @param {character[][]} board
    # @return {boolean}
    # 居然通过了，我都没想到能一遍通过，害我写了这么长的test case
    def isValidSudoku(self, board):
        sets = [set() for i in range(27)]
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch != '.':
                    if ch in sets[i] or ch in sets[9+j] or ch in sets[18+i//3*3+j//3]:
                        return False
                    else:
                        sets[i].add(ch)
                        sets[9+j].add(ch)
                        sets[18+i/3*3+j/3].add(ch)
        return True

A = Solution()
a = [['5','3','.','.','7','.','.','.','.'],
     ['.','.','.','1','9','5','.','.','.'],
     ['.','9','8','.','.','.','.','6','.'],

     ['8','.','.','.','6','.','.','.','3'],
     ['4','.','.','8','.','3','.','.','1'],
     ['7','.','.','.','2','.','.','.','6'],

     ['.','6','.','.','.','.','2','8','.'],
     ['.','.','.','4','1','9','.','.','5'],
     ['.','.','.','.','8','.','.','7','9'],
     ]
print A.isValidSudoku(a)

