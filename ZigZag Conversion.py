#coding=utf-8
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    # 注意总结规律：
    # a，b分别是（0,2n-1）里的两个系数，当a-b=2（r-1），是上边一行的单点，a==b是下边一行的单点
    # 其他则是该范围的两个点，按照每一行的值进行对应
    def convert(self, s, numRows):
        res = ""
        if numRows < 2:
            return s
        size = len(s)
        times = size/(2*(numRows-1))+1
        for i in range(numRows):
            for j in range(times):
                a = 2 * (numRows-1) * j + i
                b = 2 * (numRows-1) * (j+1) - i
                if a < size and (a == b or b - a == 2*(numRows - 1)):
                    res += s[a]
                else:
                    if a < size:
                        res += s[a]
                    if b < size:
                        res += s[b]
        return res

A = Solution()
print A.convert("PAYPALISHIRING",1)