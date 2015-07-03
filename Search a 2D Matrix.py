#coding=utf-8
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    # 这个题感觉要往四个方向走，其实只需要往右边和下边走就行
    def searchMatrix(self, matrix, target):
        i = 0
        j = 0
        height = len(matrix)
        if not height:
            return False
        width  = len(matrix[0])
        while i< height and j < width and matrix[i][j] != target:
            if j+1 < width:
                if matrix[i][j+1] > target:
                    return False
                if i+1 < height and matrix[i+1][j] <= target:
                    i += 1
                    continue
                else:
                    j += 1
            else:
                i += 1
                continue
        if i < height and j < width:
            return True
        else:
            return False




A = Solution()
a = [  [1,   3,  5,  7],
       [10, 11, 16, 20],
       [23, 30, 34, 50] ]
print A.searchMatrix(a,0)
print A.searchMatrix(a,60)
print A.searchMatrix(a,11)
print A.searchMatrix(a,13)
print A.searchMatrix(a,50)
print A.searchMatrix(a,1)
print A.searchMatrix(a,7)
print A.searchMatrix(a,23)