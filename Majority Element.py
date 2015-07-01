#coding=utf-8
import sys
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    """ 我的方法利用dict或者说map，利用的时间复杂度和空间复杂度其实还是有点高的
        别人的方法更好！"""

    def majorityElement(self, nums):
        count = 0
        majority = 0
        for num in nums:
            if count == 0:
                majority = num
                count = 1
            elif num == majority:
                count += 1
            else:
                count -= 1
        return majority

    """
    def majorityElement(self, nums):
        times = {}
        for num in nums:
            if num not in times:
                times[num] = 1
            else:
                times[num] += 1
            if times[num] >= (len(nums)*0.5):
                return num
        return None
    """

A = Solution();
nums1 = [4,3,4,5,4,3,4]
nums2 = [4,3,4,5,4,3,4,6]
nums3 = [4,3,4,3,4,3,4]
print A.majorityElement(nums1)
print A.majorityElement(nums2)
print A.majorityElement(nums3)