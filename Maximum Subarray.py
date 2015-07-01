#coding=utf-8
import sys
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    # 其实最优的 方法我想到了，但是没有继续论证，顺着遍历，和小于0就可以从下一个数开始
    # 当时我想，和小于0，会不会说下一个序列的起始点可能在当前点之前，其实是不可能的！
    # 进一步优化，分而治之，应该如何做呢，我的方法是用分治法做的：
    # 最佳结果要么是左半部分，要么在右半部分，要么包含中间两个元素，但是并不快，关键在于包含部分计算量较大

    def maxSubArray(self, nums):
        res = 0
        sum = 0
        for num in nums:
            sum += num
            res = max(sum,res)
            sum = max(sum,0)
        return res

    """
    def maxSubArray(self, nums):
        len_v = len(nums)
        min_v = - sys.maxint
        if(len_v == 0):
            return min_v
        if(len_v == 1):
            return nums[0]
        part_of_len = len_v/2
        left_v = min_v
        sum = 0
        for i in range(part_of_len-1,-1,-1):
            sum += nums[i]
            left_v = max(left_v,sum)
            #if(sum < 0):
            #   break
        right_v = min_v
        sum = 0
        for i in range(part_of_len,len_v):
            sum += nums[i]
            right_v = max(right_v,sum)
           # if(sum < 0):
           #     break;
        left_min = self.maxSubArray(nums[0:part_of_len])
        right_min = self.maxSubArray(nums[part_of_len:len_v])
        #print left_v,right_v,left_min,right_min
        res = max(left_min,right_min)
        res = max(res,left_v+right_v)
        return res
    """

A = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
print A.maxSubArray(a)
