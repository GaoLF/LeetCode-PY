class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        res = []
        vec = []
        temp = []
        candidates.sort()
        for i in range(len(candidates)):
          #  print vec
            for j in range(len(vec)):
                iter = vec[j]
                sum = 0
                for val in iter:
                    sum += val
                if sum + candidates[i] < target:
                    temp = iter[:]
                    temp.append(candidates[i])
                    vec.append(temp)
                if sum + candidates[i] == target:
                    temp = iter[:]
                    temp.append(candidates[i])
                    if temp not in res:
                        res.append(temp)
            if candidates[i] < target:
                vec.append([candidates[i]])
            if candidates[i] == target:
                temp = [candidates[i]][:]
                if temp not in res:
                    res.append(temp)
        return res




A = Solution()
print A.combinationSum2([10,1,2,7,6,1,5],8)
print A.combinationSum2([10,1,2,7,6,1,5],1)
print A.combinationSum2([10],8)
print A.combinationSum2([],8)