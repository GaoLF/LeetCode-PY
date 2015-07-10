#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    # 原理很简单，想想应该就能出来，从[]后往前找，找到第一个左边数比右边相邻数小的位置i-1 i
    # 然后从[i,size)右往左，第一个比i-1的数小的数，然后交换他俩的位置，然后将[i,size)排序
    def nextPermutation(self, nums):
        size = len(nums)
        for i in range(size-1,0,-1):
            if nums[i-1] < nums[i]:
                for j in range(size-1,i-1,-1):
                    #print j,i-1,size-1
                    if nums[j] > nums[i-1]:
                        nums[i-1],nums[j] = nums[j],nums[i-1]
                        temp = nums[i:size]
                        temp.sort()
                        nums[i:size] = temp
                        return
        else:
            nums[:] = nums[::-1]

A = Solution()
a = [2,2,0,4,3,1]
b,c,d=[3,2,1],[1,1,5],[1,5,1]
A.nextPermutation(a)
A.nextPermutation(b)
A.nextPermutation(c)
A.nextPermutation(d)
print a
print b
print c
print d