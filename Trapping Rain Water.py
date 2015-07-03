class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_v =
        while left < right:
            if height[left] <= height[right]:


A = Solution()
#print A.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print A.trap([4,2,3])