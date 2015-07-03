import copy
class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        i = j = 0
        while i < m:
            while j < n and nums2[j] < nums1[i+j]:
                print i,j,nums2[j]
                nums1.insert(i+j,nums2[j])
                j += 1
            i += 1
        while j < n:
            nums1[i+j] = nums2[j]
            j += 1
        nums1[:] = nums1[0:m+n]

A = Solution()
a = [1,3,5,6,7,8,9,20,22]
b = [2,4,6,7,8]
A.merge(a,5,b,4)
print a