#coding=utf-8
import copy

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    # 我就是头猪，还不如第一遍的时候会做，我想着是比如[1,2,3]
    # 想[]里加a,b,c,然后在[a],[b],[c]里在分别加，这样做无疑是很难做的
    # 实际应该一个一个往集合里加[] ,先加a,组成[][a]，然后再加b：[][a][b][ab]
    # 每次在之前的集合里每一个里添加一个下一个整数
    def subsets(self, nums):
        res = [[]]
        nums.sort()
        for num in nums:
            size = len(res)
            for i in range(size):
                temp = list(res[i])
                temp.append(num)
                res.append(temp)
        return res


A = Solution()
a = A.subsets([4,3,2,1])
print a