class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        height = len(matrix)
        if not height:
            return
        width = len(matrix[0])
        coors = []
        for i in range(height):
            for j in range(width):
                if not matrix[i][j]:
                    coors.append((i,j))
        for iter in coors:
            for i in range(width):
                matrix[iter[0]][i] = 0
            for i in range(height):
                matrix[i][iter[1]] = 0

A = Solution()
a = [[1,2,3],[2,0,1],[3,1,2]]
b = [[1]]
c = [[1,2,3,0]]
d = [[1,0,2],[2,3,1],[2,3,0]]
A.setZeroes(a)
A.setZeroes(b)
A.setZeroes(c)
A.setZeroes(d)
print a
print b
print c
print d
