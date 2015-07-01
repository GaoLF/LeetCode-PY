#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    #我想用bitmap的方法，居然想了半天想不出来
    #虽然想到了状态机，00--1-->01 01--1-->10 10--1-->00
    def singleNumber(self, nums):
        a = 0
        b = 0
        for num in nums:
            temp = b&num
            b = b^num
            a = a|temp
            temp = a&b
            a = a^temp
            b = b^temp
        return b

A = Solution()
print A.singleNumber([1,2,3,3,5,2,2,3,1,1])