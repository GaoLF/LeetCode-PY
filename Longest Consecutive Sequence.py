#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    # 往set里添加整数，如果是正数，会按照大小，如果是负数，则会按照先正数再负数的顺序
    # 我先取nums的最小值，然后每个值减去这个最小值加入到set中，保证set中的数最小是0
    # 然后set中的数就都是按顺序排好的，然后后面的就简单了！
    def longestConsecutive(self, nums):
        s = set([])
        p = min(nums)
        for num in nums:
            s.add(num-p)
        if not nums:
            return 0
        res = 1
        flag = 0
        s = list(s)
        for i in range(1,len(s)):
            if s[i] - s[i-1] == 1:
                if not flag:
                    flag = 1
                    temp = 2
                else:
                    temp += 1
            else:
                temp = 1
                flag = 0
            res = max(res, temp)
        return res


A = Solution()
print A.longestConsecutive([0,-1,-2,3,2,1])
print A.longestConsecutive([100, 4, 200, 1, 3, 2])