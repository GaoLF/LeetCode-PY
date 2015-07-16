class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        res = [0 for i in xrange(len(nums))]
        product = 1
        flag = 0
        i = 0
        while i < len(nums):
            if nums[i]:
                product *= nums[i]
            else:
                temp = i
                flag += 1
            i += 1
        if flag == 1:
            res[temp] = product
        elif not flag:
            for i in xrange(len(nums)):
                res[i] = product/nums[i]
        return res

A = Solution()
print A.productExceptSelf([1,2,3,4])
print A.productExceptSelf([1,2,3,4,0])
print A.productExceptSelf([1,2,3,4,0,0])
