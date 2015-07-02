#coding=utf-8
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        size = len(height)
        left = 0
        right = size - 1
        res = 0
        while left <= right:
            res = max(res,min(height[left],height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res

A = Solution()
print A.maxArea([1,2,3,4,4,3,2,1])
print A.maxArea([1])
print A.maxArea([1,2])
print A.maxArea([1,2,3])