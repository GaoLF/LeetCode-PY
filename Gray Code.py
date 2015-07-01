class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if not n:
            return None
        res = [0]
        for i in range(0, 2 ** n):
            for j in range(0, n):
                temp = 1 << j
               # print self.isOK(0,1)
               # print temp,res[i]
                if self.isOK(temp + res[i], res[i]) and temp + res[i] not in res:
                    res.append(res[i] + temp)
                    break
                if self.isOK(res[i] - temp, res[i]) and res[i] - temp not in res:
                    res.append(res[i] - temp)
                    break
        return res

    def isOK(self, num1, num2):
        foo = temp = num1 ^ num2
        i = 0
        #print '!',temp
        while temp > 0:
            temp = temp >> 1
            i += 1
        if foo == ( 1 << abs(i - 1) ):
            return True
        else:
            return False

A = Solution()

print A.isOK(1,2)
print A.isOK(3,4)
print A.isOK(0,5)
print A.isOK(3,7)
print A.grayCode(0)
print A.grayCode(1)
print A.grayCode(2)
print A.grayCode(3)
print A.grayCode(4)