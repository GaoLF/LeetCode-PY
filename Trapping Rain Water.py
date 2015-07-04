#coding=utf-8
class Solution:
    # @param {integer[]} height
    # @return {integer}
    # 为了寻找O(n)时间，O(1)的算法，我试了好多次都没有成功
    # 这个题从两端往中间走，在两边分别设置一个最大值，我之前的做法就是只设立了一个左边的，结果右边的无法求解
    # 设立左边和右边两个left right，left的高度小于right的高度，则从左边开始算，然后与左边的最大值比，比他大替换最大值
    # 比他小，res加上最大值与最小值之间的结果
    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_v = right_v =0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_v:
                    res += (left_v - height[left])
                else:
                    left_v = height[left]
                left += 1
            else:
                if height[right] < right_v:
                    res += right_v - height[right]
                else:
                    right_v = height[right]
                right -= 1
        return res
    """
    def trap(self, height):
        if not height:
            return 0
        max_v = height[0]
        max_f = 0
        res = 0
        i = 0
        while max_f + 1  < len(height):
            if i == len(height):
                max_f += 1
                i = max_f
                max_v = height[i]
            if height[i] >= max_v:
                water = 0
                for j in range(max_f,i):
                    water += height[j]
                res += (max_v*(i - max_f ) - water)
                max_f = i
                max_v = height[i]
            i += 1
        return res
    """

A = Solution()
print A.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print A.trap([4,2,3])
print A.trap([])
print A.trap([1])