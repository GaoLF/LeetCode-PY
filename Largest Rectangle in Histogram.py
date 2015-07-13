class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        size = len(height)
        if not size:
            return 0
        if size == 1:
            return height[0]
        height.append(0)
        res = 0
        peek = []
        i = 0
        while i < size + 1:
            if len(peek) == 0 or height[i] > height[peek[-1]]:
                peek.append(i)
                i += 1
            else:

                h = height[peek[-1]]
                del(peek[-1])
                if len(peek) == 0:
                    step = i
                else:
                    step = i - peek[-1] - 1
              #  print i,h,step,"!",peek,"!",res
                res = max((h * step), res)

        return res

A = Solution()
print A.largestRectangleArea([1,2,3,4,5])
print A.largestRectangleArea([2,1,5,6,2,3])
print A.largestRectangleArea([2,1,5,1,2,3])
print A.largestRectangleArea([2,1,5,1,2,2,2,2,3])