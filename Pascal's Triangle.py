class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if not numRows:
            return []
        res = [[1]]
        for i in range(numRows-1):
            last = res[i]
            to_insert = []
            to_insert.append(1)
            for j in range(1,i+1):
                to_insert.append(last[j-1]+last[j])
            to_insert.append(1)
            res.append(to_insert)
        return res

A = Solution()
print A.generate(0)
print A.generate(1)
print A.generate(5)