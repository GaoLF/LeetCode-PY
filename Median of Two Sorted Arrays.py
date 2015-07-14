class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        if not len1 and not len2:
            return 0
        size = (len1+len2)/2
        i = j = 0
        if (len1 + len2)%2:
            size += 1
        while size:
            if i < len1 and j < len2:
                if nums1[i] < nums2[j]:
                    res = nums1[i]
                    i += 1
                else:
                    res = nums2[j]
                    j += 1
            elif i < len1:
                res = nums1[i]
                i += 1
            else:
                res = nums2[j]
                j += 1
            size -= 1
        if i < len1 and j < len2:
            res2 = min(nums1[i],nums2[j])
        elif i < len1:
            res2 = nums1[i]
        elif j < len2:
            res2 = nums2[j]
        else:
            return res
        #print res,res2
        if (len1 + len2)%2 == 0:
            return float(res + res2)/2
        else:
            return float(res)


A = Solution()
print A.findMedianSortedArrays([2,3,4],[1,4,5])