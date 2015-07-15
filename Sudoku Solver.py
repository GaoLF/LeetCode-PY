class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        s = [set([]) for i in xrange(27)]
        for i in xrange(9):
            for j in xrange(9):
                c = board[i][j]
                if c != '.':
                    s[i].add(c)
                    s[9+j].add(c)
                    s[18 + i/3*3+j/3].add(c)
        self.solve(board,0,0,s)


    def solve(self,board,i,j,s):
        if j == 9:
            j = 0
            i += 1
        if i == 9:
            return 1
        #c = board[i][j]
        if board[i][j] != '.':
            return self.solve(board,i,j+1,s)
        else:
           # print i,9+j,18+i/3*3+j/3
            for c in ['1','2','3','4','5','6','7','8','9']:
                if (c not in s[i]) and (c not in s[9 + j]) and (c not in s[18+i/3*3+j/3]):
                    s[i].add(c)
                    s[9+j].add(c)
                    s[18+i/3*3+j/3].add(c)
                    board[i][j] = c
                    if self.solve(board,i,j+1,s):
                        return 1
                    s[i].remove(c)
                    s[9+j].remove(c)
                    s[18+i/3*3+j/3].remove(c)
                    board[i][j] = '.'
        return 0


A = Solution()
a = [['5','3','.','.','7','.','.','.','.'],
     ['6','.','.','1','9','5','.','.','.'],
     ['.','9','8','.','.','.','.','6','.'],

     ['8','.','.','.','6','.','.','.','3'],
     ['4','.','.','8','.','3','.','.','1'],
     ['7','.','.','.','2','.','.','.','6'],

     ['.','6','.','.','.','.','2','8','.'],
     ['.','.','.','4','1','9','.','.','5'],
     ['.','.','.','.','8','.','.','7','9'],
     ]
A.solveSudoku(a)
print a
x = set([1,2,3,4])
y = set([2,3,5,8])
#print x and y