class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        size = len(nums)
        nums.sort()
        if size < 3:
            return 0
        sum = nums[0] + nums[1] + nums[2]
        for i in range(size-2):
            m = i+1
            n = size-1
            while m < n:
                temp = nums[i] + nums[m] + nums[n]
                if abs(sum - target) > abs(target - temp):
                    sum = temp
                if temp < target:
                    m += 1
                else:
                    n -= 1
        return sum


A = Solution()
print A.threeSumClosest([-1,2,1,-4],-7)
print A.threeSumClosest([],-7)
print A.threeSumClosest([1,2,4,8,16,32,64,128], 82)


