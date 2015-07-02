import copy
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        res = []
        for num in nums:
            if not len(res):
                temp = []
                temp.append(num)
                res.append(temp)
            else:
                temp = []
                for iter in res:
                    #print iter,"!"
                    len_i = len(iter)
                    for i in range(0,len_i+1):
                        l = copy.deepcopy(iter)
                        l.insert(i,num)

                        #print l,iter
                        #print l,i,num,temp
                        if l not in temp:
                            #print temp,l
                            temp.append(l)
                         #   print temp,"!"
                res = temp
        return res

A = Solution()
print A.permute([1,2,3])
print A.permute([1,2])
print A.permute([1])