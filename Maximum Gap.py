#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    # 我是用一个桶排序的方法做的，但是不知道这样是不是和正规的桶排序一致
    # 求出最小间隔(max_v - min_v)/len(nums)，把所有数分成len(num)份
    # 然后每个数遍历，每一份一个[]，存放在该dict中
    # 然后遍历dict，查找相邻的两个有值的桶的，最小值减去上一个有值的桶的最大值作为res，去最大res
    # 但是有一个地方需要注意，第一次提交结果就错了，就是left的值不能设置成0 ，应该是num的最小值
    def maximumGap(self, nums):
        dic = {}
        if len(nums) < 2:
            return 0
        min_v = min(nums)
        max_v = max(nums)
        size = (max_v - min_v)/len(nums)
        if not size:
            size = 1
        for num in nums:
            if (num-min_v)/size in dic:
                dic[(num-min_v)/size].append(num)
            else:
                dic[(num-min_v)/size]=[num]
       # print dic
        res = 0
        left = min_v
        right = 0
        for i in range(len(nums)+1):
            if i in dic:
                res = max(res,min(dic[i]) - left)
                left = max(dic[i])
        return res

A = Solution()
print A.maximumGap([1,2,3])
print A.maximumGap([15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740])
print A.maximumGap([1,5,2,18,7,10,20,100])