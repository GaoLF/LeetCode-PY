class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        size1 = len(a)
        size2 = len(b)
        size = max(size1,size2)
        a = '0'*(size-size1) + a
        b = '0'*(size-size2) + b
        flag = 0
        res = ''
        for i in range(size-1,-1,-1):
            t1 = int(a[i])
            t2 = int(b[i])
            if flag:
                if t1 and t2:
                    res = '1' + res
                elif t1 or t2:
                    res = '0' + res
                else:
                    res = '1' + res
                    flag = 0
            else:
                if t1 and t2:
                    flag = 1
                    res = '0' + res
                elif t1 or t2:
                    res = '1' + res
                else:
                    res = '0' + res
        if flag:
            res = '1' + res
        return res

A = Solution()
print A.addBinary("1010","11")
print A.addBinary("10","11")
print A.addBinary("","")

