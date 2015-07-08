class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        vec = [-1<<31 for i in range(k)]
        if not k:
            return 0
        for num in nums:
            if vec[0] < num:
                i = 0
                while i < k and vec[i] < num:
                    i += 1
                i -= 1
                for j in range(0,i,1):
                    vec[j] = vec[j+1]
                vec[i] = num
        return vec[0]

        #print vec

A = Solution()
print A.findKthLargest([1,3,2,4],1)
print A.findKthLargest([3,2,1,5,6,4],6)