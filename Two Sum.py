class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        s = {}
        for i in xrange(len(nums)):
            temp = target - nums[i]
            if temp in s:
                return [s[temp] + 1, i + 1]
            else:
                s[nums[i]] = i


A = Solution()
print A.twoSum([2,7,11,15],9)