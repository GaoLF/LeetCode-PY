# coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
    # 还有注意的是，是判断到不到最后一个元素，不是到size
    # 空的时候我怎么知道能不能到达
        i = 0
        size = len(nums)
        if not size:
            return False
        while i < size-1:
            if not nums[i]:
                for j in range(i-1,0,-1):
                    if j + nums[j] > i:
                        i = j + nums[j]
                        break
                else:
                    return False
            else:
                i += nums[i]
        return True

    """
    # 不能用递归，ob的测试很多1 RuntimeError: maximum recursion depth exceeded
    def canJump(self, nums):
        dic = set()
        return self.jump(nums,0,dic)
    def jump(self,nums,i,dic):
        if i + nums[i] >= len(nums):
            return True
        if not nums[i]:
            dic.add(i)
        if i in dic:
            return False
        for j in range(nums[i],0,-1):
            if self.jump(nums,i + j,dic):
                return True
            else:
                dic.add(i + j)
                return False
        return False
        """

A = Solution()
print A.canJump([0])
print A.canJump([2,3,1,1,4,0,0,0,0])
print A.canJump([2,3,1,1,4])
print A.canJump([3,2,1,0,4])