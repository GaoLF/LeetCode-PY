class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        i = j = 0
        k = len(nums)
        if not nums:
            return None
        while i < k:
            if nums[i] == 0:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1
            elif nums[i] == 2:
                nums[k-1],nums[i] = nums[i],nums[k-1]
                k -= 1
                i -= 1
            i += 1
        return nums

A = Solution()
print A.sortColors([])
print A.sortColors([0])
print A.sortColors([0,1])
print A.sortColors([0,2,1,2,1,0,0,2,1])