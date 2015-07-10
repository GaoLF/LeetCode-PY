#coding=utf-8
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    # 我这个笨蛋，想了半天还是没有想出来怎么解，最后还是用的之前的C++方法，还是别人的方法
    # 从前往后进行解，然后如果和大于了s，则从前边开始减
    def minSubArrayLen(self, s, nums):
        begin = 0
        i = 0
        sum = 0
        res = 1<<31
        while i <= len(nums):
            #print i,begin,sum,res
            if sum >= s:
                res = min(res,i - begin)
                sum -= nums[begin]
                begin += 1
            else:
                if i < len(nums):
                    sum += nums[i]
                i += 1
        if res == 1<<31:
            return 0
        return res

A = Solution()
print A.minSubArrayLen(1,[])