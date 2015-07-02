class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        size = len(matrix)
        for i in range(0,size/2):
            for j in range(i,size-i-1):
                temp = matrix[i][j]
                len_v = size - i
                matrix[i][j] = matrix[size-j-1][i]
                matrix[size-j-1][i]=matrix[size-i-1][size-j-1]
                matrix[size-i-1][size-j-1]=matrix[j][size-i-1]
                matrix[j][size-i-1] = temp


A = [[1]]
B = Solution()
B.rotate(A)
print A
A = [[1,2],[3,4]]
B = Solution()
B.rotate(A)
print A
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = Solution()
B.rotate(A)
print A