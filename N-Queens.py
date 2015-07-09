#coding=utf-8
class Solution:
    # @param {integer} n
    # @return {string[][]}
    # 之前都用乱七八糟的方法，刚看到用bitmask的方法不错
    # 取当前位的时候，给当前传给下一位一个mask即所有已经占用的位置，不能用的位置
    # 当前位置如果可用，则必须与mask相或且结果为0
    def solveNQueens(self, n):
        res = [0]
        temp = ['.'*n for i in range(n)]
       # print temp
        self.solve(0,n,0,0,0,res,temp)
        return res[0]

    def solve(self,row,n,left_shift,ver,right_shift,res,temp):
        if row >= n:
            res[0] += 1
            return
        mask = left_shift|ver|right_shift
        i = 0
        while i < n:
            b = 1 << i
            if not b & mask:
               # print temp
                temp[row] = i*'.' + "Q" + (n-i-1)*'.'
              #  print temp
                self.solve(row+1,n,(left_shift|b)<<1,ver|b,(right_shift|b)>>1,res,temp)
                temp[row] = '.'*n
            i += 1

A = Solution()
print A.solveNQueens(8)
