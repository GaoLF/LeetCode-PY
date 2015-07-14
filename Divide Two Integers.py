class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if divisor == 0 or dividend == 0:
           return 0
        sign = ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0))
        dividend,divisor = abs(dividend),abs(divisor)
        res = 0
        flag = 1
        temp = divisor
        while dividend >= temp:
           res += flag
           dividend -= divisor
           if dividend > divisor*2:
               divisor *= 2
               flag *= 2
           elif dividend < divisor:
               divisor = temp
               flag = 1
        res = res *((-1)**sign)
        if res >= 1<<31:
            res = (1<<31)-1
        if res <= -1<<31:
            res = -1<<31
        return res

A = Solution()
print A.divide(3,1)
print A.divide(-10,3)
print A.divide(125,5)
print A.divide(1254243,543)
print A.divide(1432432,1)
print A.divide(43243,-5)
print A.divide(-1<<31,1),-1<<31
print A.divide(1<<31,1),1<<31
print A.divide(-1<<31,-1),1<<31
print A.divide(1<<31,-1),1<<31