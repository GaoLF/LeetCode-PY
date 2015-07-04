class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def getRow(self, rowIndex):
        if not rowIndex:
            return [1]
        res = [1]
        for i in range(rowIndex):
            last = res
            res = []
            res.append(1)
            for j in range(1,i+1):
                res.append(last[j-1]+last[j])
            res.append(1)
        return res

A = Solution()
print A.getRow(0)
print A.getRow(1)
print A.getRow(2)
print A.getRow(3)
print A.getRow(4)
print A.getRow(5)