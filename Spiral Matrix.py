#coding=utf-8
class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    # 第一遍没看清楚这个矩阵的长宽可以不一样大，第二次就是你如果输入一个[],应该返回一个[]，我返回了一个None
    def spiralOrder(self, matrix):
        if not matrix:
            return None
        res = []
        height = len(matrix)
        width = len(matrix[0])
        size = height*width
        m = 0
        while len(res)<size:
            for i in range(0,width):
                if matrix[m][i] not in res:
                    res.append(matrix[m][i])
            for i in range(0,height):
                if matrix[i][width-m-1] not in res:
                    res.append(matrix[i][width-m-1])
            for i in range(width-1,-1,-1):
                if matrix[height-m-1][i] not in res:
                    res.append(matrix[height-m-1][i])
            for i in range(height-1,-1,-1):
                if matrix[i][m] not in res:
                    res.append(matrix[i][m])
            m += 1
        return res

A = Solution()
print A.spiralOrder([])
print A.spiralOrder([[1]])
print A.spiralOrder([[1,2],[3,4]])
print A.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print A.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print A.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
