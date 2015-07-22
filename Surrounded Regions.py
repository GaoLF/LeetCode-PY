class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        row = len(board)
        if not row:
            return 0
        col = len(board[0])
        for i in xrange(row):
            self.check(board,i,0,row,col)
            if col > 1:
                self.check(board,i,col - 1,row,col)
        for i in xrange(col):
            self.check(board,0,i,row,col)
            if row > 1:
                self.check(board,row - 1,i,row,col)
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '1':
                    board[i][j] = 'O'

    def check(self,vec,i,j,row,col):
        if vec[i][j] == 'O':
            vec[i][j] = '1'
            if i-1 > 0:
                self.check(vec,i-1,j,row,col)
            if i+1 < row:
                self.check(vec,i+1,j,row,col)
            if j-1 > 0:
                self.check(vec,i,j-1,row,col)
            if j+1 < col:
                self.check(vec,i,j+1,row,col)

A = Solution()
a = [['X', 'X', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'X', 'O', 'X'],
     ['X', 'O', 'X', 'X']]
A.solve(a)
print a