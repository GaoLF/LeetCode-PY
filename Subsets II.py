class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        for num in nums:
            size = len(res)
            for i in range(size):
                temp = list(res[i])
                temp.append(num)
                if temp not in res:
                    res.append(temp)
        return res


A = Solution()
print A.subsetsWithDup([4,3,2,1])
print A.subsetsWithDup([1,1,1,1,1])
print A.subsetsWithDup([1,2,2])
