class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        nums[:] = [x for x in nums if x != val]
        return len(nums)
    def change(self,l):
        l .append(2)

A = Solution()
print A.removeElement([1,2,3,4,5,3,2,2],2)
print A.removeElement([1,2,3,4,5,3,2,2],1)
print A.removeElement([1,2,3,4,5,3,2,2],3)
print A.removeElement([1,2,3,4,5,3,2,2],0)
print A.removeElement([4,5],4)

nums = [1,2,3,4,5,6,1]
A.removeElement(nums,1)
print nums

l = [1]
A.change(l)
print l