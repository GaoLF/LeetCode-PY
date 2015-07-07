class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if not x:
            return 0
        if not n:
            return 1
        if n < 0:
            x = 1/x
            n = abs(n)
        temp = 1
        res = 1
        y = x
        while n:
            if n >= temp:
                res *= x
                n -= temp
                x *= x
                temp += temp
            else:
                temp = 1
                x = y
           # print n,temp
        return res

A = Solution()
print A.myPow(2,4)
print A.myPow(0.5,-4)
print A.myPow(2,10)
print A.myPow(2,4)



