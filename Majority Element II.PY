class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 2
            for key in dic.keys():
                if key == num:
                    dic[key] += 2
                elif len():
                    dic[key] -= 1
                    if dic[key] <= 0:
                        del(dic[key])
        return [i for i in dic.keys()]


a = {1:2,2:3}
#print a
#print [i for i in a.values()]
#print len(a)
A = Solution()
print A.majorityElement([1,2,3,1,2,3,1,2,3])
print A.majorityElement([1,2,3,1,1,1,1,1,1])
print A.majorityElement([1,2,3,2,3,3,5,6,7])