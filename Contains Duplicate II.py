class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        s = set()
        size = len(nums)
        k = min(k,size - 1)
        for i in range(size):
            s.add(nums[i])
            if i >= k:
                s.add(nums[i])
                if len(s) < k + 1:
                    return True
                s = s - set([nums[i-k]])
        return False

A = Solution()
print A.containsNearbyDuplicate([1,2,3,4,5,6,7],2)
print A.containsNearbyDuplicate([1,2,3,1,2,3,4],2)
print A.containsNearbyDuplicate([1,2,3,1,2,3,4],3)
print A.containsNearbyDuplicate([1,2,3,1,2,3,4],4)
print A.containsNearbyDuplicate([1,1],1)
print A.containsNearbyDuplicate([2],0)