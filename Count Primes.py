#coding=utf-8
class Solution:
    # @param {integer} n
    # @return {integer}
    # 素数检测
    # 我这个方法还是会有很多重复的计算
    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = 0
        flag = [True for i in xrange(n)]
        for i in xrange(n):
            if not i%2:
                flag[i] = False
        for i in xrange(2,int(n**0.5)+1):
            if flag[i]:
                j = i * 2
                while j < n:
                    flag[j] = False
                    j += i
        flag[2] = True
        flag[1] = False
        #print flag
        for i in flag:
            if i:
                res += 1
        return res

A = Solution()
for i in xrange(20):
    print A.countPrimes(i)
