class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        stairs = [1,1]
        if not n:
            return 0
        for i in range(2,n+1):
            stairs.append( stairs[i-1] + stairs[i-2] )
        return stairs[n]

A = Solution()
print A.climbStairs(0)
print A.climbStairs(1)
print A.climbStairs(2)
print A.climbStairs(3)
print A.climbStairs(4)
print A.climbStairs(5)