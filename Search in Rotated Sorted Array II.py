class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return False
        size = len(nums)
        if target < nums[0]:
            if nums[0] < nums[size - 1]:
                return False
            else:
                i = size - 1
                while i >= 0 and target < nums[i]:
                    i -= 1
                if i >= 0 and target == nums[i]:
                    return True
                else:
                    return False
        else:
            i = 0
            while i < size and target > nums[i]:
                i += 1
            if i < size and target == nums[i]:
                return True
            else:
                return False

A = Solution()
print A.search([0,2,4,4,6,6,6,8,10],9)
print A.search([0,2,4,6,8,10],8)
print A.search([8,10,0,2,4,6],9)
print A.search([8,10,0,2,4,4,6,6],4)
print A.search([8,10,0,2,4,6],5)
print A.search([0],9)
print A.search([],9)
print A.search([0],0)

