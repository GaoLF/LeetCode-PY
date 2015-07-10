#coding=utf-8
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
    # 我这方法都有点胡编的，但是最后居然还能作对，就是从m开始加
    # 一次加上一个该数拖尾0的个数i的1<<i的数
    # 然后每次按位与该数
        i = 0
        temp = m
        res = m
        if not m:
            return 0
        while m < n:
            temp = m
            i = 0
            while not temp % 2:
                temp >>= 1
                i += 1
            res = res & m
            m += (1<<i)
        return res & n

A = Solution()
a = 0x10101
b = 0x11011
print A.rangeBitwiseAnd(a,b)


res = a
for i in range(a,b+1):
    res = i&res
print res