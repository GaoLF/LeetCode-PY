class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.check(candidates,0,0,target,res,[])
        return res

    def check(self,c,sum_v,j,t,res,temp_l):
        for i in range(j,len(c)):
            if sum_v + c[i] == t:
                temp_l.append(c[i])
                if temp_l not in res:
                    #print temp_l
                    res.append(temp_l)
                return
            elif sum_v + c[i] < t:
                temp = temp_l[:]
                temp.append(c[i])
                self.check(c,sum_v+c[i],i,t,res,temp)
            else:
                return

A = Solution()
print A.combinationSum([2,3,6,7],1)
print A.combinationSum([2,3,6,7],2)
print A.combinationSum([2,3,6,7],7)
print A.combinationSum([12,2,3,5,9,6,7],12)