class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        a=[]
        for i in range(0,m):
            for j in range(0,n):
                up = 0
                left = 0
                if not i and not j:
                    up = 1
                if i  > 0:
                    up = a[(i - 1) * n + j]
                if j  > 0:
                    left = a[i * n + j - 1]
                a.append(up + left)
        return a[m * n - 1]

A = Solution()
print A.uniquePaths(3,2)
print A.uniquePaths(3,7)
print A.uniquePaths(3,4)