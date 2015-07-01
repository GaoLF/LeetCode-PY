class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        len_v = len(nums)
        if not nums:
            return None
        if nums[0] <= nums[len_v-1]:
            return nums[0]
        else:
            temp = nums[0]
            for num in nums:
                if num < temp:
                    return num
                else:
                    temp = num
            return nums[len_v-1]

A = Solution()
print A.findMin([0])
print A.findMin([1,2,3,4,5,6,7])
print A.findMin([4,5,6,7,0,1,2])