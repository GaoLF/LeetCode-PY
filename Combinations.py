import copy
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if not n or not k:
            return []
        res = []
        for i in range(k):
            if not res:
                for j in range(n):
                    res.append([j+1])
            else:
                temp = []
                for iter in res:
                    tail = iter[len(iter)-1]
                    if tail < n:
                        for m in range(tail+1,n+1):
                            temp_iter = copy.deepcopy(iter)
                            temp_iter.append(m)
                            temp.append(temp_iter)
                res = temp
        return res

A = Solution()
print A.combine(4,1)
print A.combine(4,2)
print A.combine(4,3)
print A.combine(4,4)


