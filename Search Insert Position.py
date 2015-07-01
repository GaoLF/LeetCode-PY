class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        res = 0
        for num in nums:
            if target > num:
                res += 1
            else:
                break
        return res


A = Solution()
nums = [1,3,5,6]
print A.searchInsert(nums,5)
print A.searchInsert(nums,2)
print A.searchInsert(nums,7)
print A.searchInsert(nums,0)