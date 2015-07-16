class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        flag = [[False for i in xrange(len(board[0]))]for j in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
               # print word[0:1],board[i][j]
                if word[0:1] == board[i][j]:
                    if self.check(word,board,0,i,j,flag):
                        return True
        return False
    def check(self,word,board,index,i,j,flag):
        #print i,j,index
        if board[i][j] != word[index:index+1]:
            return False
        if flag[i][j]:
            return False
        if index + 1 == len(word):
            return True
        flag[i][j] = True
        if i > 0:
           if self.check(word,board,index+1,i-1,j,flag):
               return True
        if i + 1 < len(board):
            if self.check(word,board,index+1,i+1,j,flag):
                return True
        if j > 0:
            if self.check(word,board,index+1,i,j-1,flag):
                return True
        if j + 1 < len(board[0]):
            if self.check(word,board,index+1,i,j+1,flag):
                return True
        flag[i][j] = False
        return False

A = Solution()
a = [['A','B','C','E'],
     ['S','F','C','S'],
     ['A','D','E','E']]
print A.exist(a,"ABCCED")
print A.exist(a,"SFCS")
print A.exist(a,"ABCB")