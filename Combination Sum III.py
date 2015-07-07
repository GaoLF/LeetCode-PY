class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        res = []
        temp = []

        def check(k,n,end,vec):
            temp = vec[:]
            if k == 1 and n <= end and n:
                temp.append(n)
                res.append(temp)
            elif k == end:
                sum = 0
                for i in range(1,k+1):
                    sum += i
                if sum == n:
                    for i in range(1,k+1):
                        temp.append(i)
                    res.append(temp)
            elif end < n:
                check(k,n,end-1,vec)
                vec.append(end)
              #  if end == 4 and temp == [4]:
               #     print k-1, n-end
                check(k-1,n-end,end-1,vec)
                vec.pop()
            else:
                check(k,n,end-1,vec)
        check(k,n,9,temp)
        return res

A = Solution()
print A.combinationSum3(3,9)