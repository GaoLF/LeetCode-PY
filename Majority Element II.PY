#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        count1,count2,candidate1,candidate2 = 0,0,0,1
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif not count1:
                candidate1 = num
                count1 += 1
            elif not count2:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        res = [candidate1,candidate2]
        return [res[i] for i in range(2) if nums.count(res[i]) > len(nums)//3]
        #return [n for n in (candidate1, candidate2)
            #if nums.count(n) > len(nums) // 3]别人写的这一句，好像更加简练！

a = {1:2,2:3}
#print a
#print [i for i in a.values()]
#print len(a)
A = Solution()
print A.majorityElement([1,2,2,1,2,1,1,2,1])
print A.majorityElement([1,2,3,1,1,1,1,1,1])
print A.majorityElement([1,2,3,2,3,3,5,6,7])