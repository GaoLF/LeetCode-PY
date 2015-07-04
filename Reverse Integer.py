#coding=utf-8
import sys
# ********************************************
# ************* -1/10 居然等于 -1**************
# ********************************************
#我在这里用sys.maxint 居然不行，得把sys.maxint 换成 2147483647 才行
class Solution:
    # @param n, an integer
    # @return an integer
    def reverse(self, x):
        res = 0
        if x > 0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        while x:
            temp = x%10
            res =  (res *10) + temp
            x /= 10
        res *= sign
        if res > sys.maxint:
            res = 0
        if res < -(sys.maxint + 1):
            res = 0
        return res

A = Solution()
#print -1/10
print sys.maxint
print A.reverse(43261596)
print A.reverse(1534236469)
print A.reverse(2147483647)
print A.reverse(-2147483647)