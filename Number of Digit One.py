class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        bits = 0
        dic = {0:0,1:0,10:1}
        res = 0
        if n <= 0:
            return 0
        while n >= 10**bits:
            bits += 1
        temp = 10**(bits - 1)
        for i in range(1,bits):
            dic[10**i] = dic[10**(i - 1)] * 10 + 10**(i-1)
        print dic
        while n >= 10:
            x = n/temp
            if x > 1:
                res += (temp)
            elif x == 1:
                res += (n % temp +1)
            res += x*(dic[temp])
            n = n % temp
            temp /= 10
        if n >= 1:
            res += 1
        return res
A = Solution()
print A.countDigitOne(11)
print A.countDigitOne(35)
print A.countDigitOne(124)
print A.countDigitOne(224)
print A.countDigitOne(1011)