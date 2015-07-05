class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        begin = 0
        end = len(nums)- 1
        while begin <= end:
            mid = (begin + end)/2
            if nums[mid] == target:
                for i in range(mid,begin-1,-1):
                    if nums[i] != target:
                        left = i + 1
                        break
                else:
                    left = begin
                for i in range(mid,end+1):
                    if nums[i] != target:
                        right = i - 1
                        break
                else:
                    right = end
                return [left,right]
            elif nums[mid] < target:
                begin = mid + 1
            else:
                end = mid -1
        return [-1,-1]

A = Solution()
print A.searchRange([5, 7, 7, 8, 8,8,8, 10],8)
print A.searchRange([8],8)
print A.searchRange([5, 7, 7, 8, 8, 10],9)