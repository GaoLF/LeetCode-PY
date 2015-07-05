class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        size = len(triangle)
        sum_l = [0 for i in range(size)]
        sum_l[0] = triangle[0][0]
        for i in range(1,size):
            temp = sum_l[:]
            for j in range(i+1):
                if not j:
                    sum_l[j] += triangle[i][j]
                elif j == i:
                    sum_l[j] =temp[j-1] + triangle[i][j]
                else:
                    sum_l[j] =min(temp[j-1],sum_l[j])+triangle[i][j]
        return min(sum_l)

A = Solution()
#print A.minimumTotal([[1],[1,2]])
print A.minimumTotal([[2],
                     [3,4],
                    [6,5,7],
                   [4,1,8,3]])
#print A.minimumTotal()