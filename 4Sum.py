class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        i,j,m,n = 0,0,0,0
        size = len(nums)
        res =[]
        if size < 4:
            return []
        while i < size - 3:
           # print i,j,m,n
            j = i + 1
            #if nums[i] > target:
            #    return res
            while j < size - 2:

                sum_2 = nums[i] + nums[j]
                #if sum_2 > target:
                #    break
                #print i,j
                m,n = j+1,size-1
                while m < n:
                    if nums[m] + nums[n] + sum_2> target:
                        n -= 1
                    elif nums[m] + nums[n] + sum_2 < target:
                        m += 1
                    else:
                        if [nums[i],nums[j],nums[m],nums[n]] not in res:
                            res.append([nums[i],nums[j],nums[m],nums[n]])
                        m += 1
                        n -= 1
                j += 1
            i+= 1
        return res

A = Solution()
print A.fourSum([1,-2,-5,-4,-3,3,3,5], -11)
