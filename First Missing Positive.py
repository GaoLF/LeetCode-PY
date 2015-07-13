#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        size = len(nums)
        for i in range(size):
            while nums[i] <= size and nums[i] > 0 and nums[nums[i] - 1] != nums[i]:
                #第一个条件是当前数在size范围内，第二个条件是正数，第三个数是当前的两个数是不相等，防止死循环
                #这个循环的目的是使得nums[i-1] = i
                #即将（0，size）范围的数i全都换到nums[i-1]中
                #print i,nums[i]
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
                #nums[i], nums[nums[i]-1]= nums[nums[i]-1],nums[i]
                #这一句有意思哈，我想实现交换，但是上边一句可以，下边一句就不可以
                # print i,nums[i]
        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        return size + 1

    """这个方法太讨巧，利用python的特性
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        for i in range(1,10000):
            if i not in nums:
                return i
    """

A = Solution()
print A.firstMissingPositive([])