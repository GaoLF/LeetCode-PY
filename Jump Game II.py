class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        res = 0
        size = len(nums)
        if not size:
            return 0
        flag = [1<<31 for i in range(size)]
        flag[0] = 0
        i = 0
        while True:
            step = nums[i]
            if step + i >= size - 1:
             #   print flag
                return flag[i] + 1
            for j in range(i + 1,step + i + 1):
                #print j,"!"
                flag[j] = min(flag[j],flag[i] + 1)
            i += 1
        #return flag[]

A = Solution()
print A.jump([0])
print A.jump([2,3,1,1,4,0,0,0,0])
print A.jump([2,3,1,1,4])
print A.jump([3,0,0,1,0])