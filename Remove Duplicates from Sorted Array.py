class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        i = 0
        while i + 1 < len(nums):
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


A = Solution()
a = [1,2,3,4,5,6,7,8,9]
print A.removeDuplicates(a),a

a = [1,1,2,2,3,4,5,5,5,6,7,8,9]
print A.removeDuplicates(a),a

a = []
print A.removeDuplicates(a),a

a = [1]
print A.removeDuplicates(a),a
#print B
#B = A[range(0,len(A),2)]
