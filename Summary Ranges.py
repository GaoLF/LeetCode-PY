class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        size = len(nums)
        if not size:
            return []
        begin = nums[0]
        begin_index = 0
        res = []
        for i in range(1,size):
            if nums[i] - begin != i - begin_index:
                temp = str(begin)
                if i - begin_index != 1:
                    temp += "->" + str(nums[i - 1])
                res.append(temp)
                begin = nums[i]
                begin_index = i
        if nums[size - 1] == begin:
            res.append(str(nums[size-1]))
        else:
            res.append(str(begin)+"->"+str(nums[size-1]))
        return res

A = Solution()
print A.summaryRanges([-1,0,1,2,4,5,7])
