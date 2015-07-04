class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        res = 0
        while n:
            n /= 5
            res += n
        return res

A = Solution()
print A.trailingZeroes(1)
print A.trailingZeroes(10)
print A.trailingZeroes(625)
print A.trailingZeroes(125)

for i in range(1,126):
    if i%5 == 0:
        a=0
 #       print i
#print x