#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    # 这个我就没好好仔细写，只是把rob一的那个题复制粘贴了一下，就是取[0,n-1)和[1,n)的取max
    # 但是需要注意的是！！当len == 1 时，直接返回nums[0]否则无解
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        start_with_zero = 0
        start_with_one  = 0
        for i in range(len(nums)-1):
            if not i%2: # start with 0
                start_with_zero = max(start_with_zero + nums[i],start_with_one)
            else:
                start_with_one = max(start_with_one + nums[i],start_with_zero)
        res1 = max(start_with_one,start_with_zero)
        start_with_zero = 0
        start_with_one  = 0
        for i in range(1,len(nums)):
            if not i%2: # start with 0
                start_with_zero = max(start_with_zero + nums[i],start_with_one)
            else:
                start_with_one = max(start_with_one + nums[i],start_with_zero)
        res2 = max(start_with_one,start_with_zero)
        return max(res1,res2)

A = Solution()
print A.rob([1,2,3,4])