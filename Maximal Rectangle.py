#coding=utf-8
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    # ******************************************************************
    # ****************可能存在更好算法，因为我的算法在分布上比较靠后************
    # 我的方法感觉又是一个比较笨的方法，测出每个点到他右边所有1的个数存在step[][]中
    # 然后每个点遍历，测每个点作为左上角的面积，求最大
    def maximalRectangle(self, matrix):
        rows = len(matrix)
        if not rows:
            return 0
        cols = len(matrix[0])
        step = [[0 for i in range(cols)] for j in range(rows)]
        res = 0
        for i in range(rows):
            for j in range(cols - 1,-1,-1):
                if matrix[i][j] == '1':
                    if j == cols - 1:
                        step[i][j] = 1
                    else:
                        step[i][j] = 1 + step[i][j + 1]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    sum = 0
                    lens = step[i][j]
                    res = max(res,lens)
                    for m in range(i + 1,rows):
                        if matrix[m][j] == '1':
                            lens = min(step[m][j],lens)
                            res = max((m - i + 1)*lens,res)
                            #print lens,m,i,res
                        else:
                            break
        return res

A = Solution()
a = [['1','1','0','0','0'],
     ['0','1','0','0','0'],
     ['1','0','0','1','0'],
     ['1','1','0','0','0'],
     ['1','1','0','0','0']]
print A.maximalRectangle(a)
a = [['0','1']]
print A.maximalRectangle(a)

