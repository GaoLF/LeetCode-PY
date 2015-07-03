class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        res = [[0 for i in range(n)] for i in range(n)]
        iter = 1
        m = 0
        while iter <= n*n:
            for i in range(0,n):
                if not res[m][i]:
                    res[m][i] = iter
                    iter += 1
            for i in range(0,n):
                #print i,n-m,n
                if not res[i][n-m-1]:
                    res[i][n-m-1] = iter
                    iter += 1
            for i in range(n-m-1,-1,-1):
                if not res[n-m-1][i]:
                    res[n-m-1][i] = iter
                    iter += 1
            for i in range(n-m-1,-1,-1):
                if not res[i][m]:
                    res[i][m] = iter
                    iter += 1
            m += 1
        return res

A = Solution()
#print A.generateMatrix(1)
print A.generateMatrix(1)
print A.generateMatrix(3)
print A.generateMatrix(4)