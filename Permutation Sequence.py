class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        vec = []
        temp = 1
        res = ""
        for i in range(1,n):
            temp *= i

        for i in range(n-1,0,-1):
            foo = (k-1)/temp
            k = k - foo*temp
            vec.append(foo + 1)
            temp /= i
        vec.append(1)
      #  print vec
        for i in range(n):
            flag = 0
            a = -1
            while flag != a:
                a = flag
                flag = 0
                for x in range(i):
                    b = 0
                    for y in range(x):
                        if res[y] <= res[x]:
                            b += 1
                    if vec[x] + b <= (vec[i] + a):
                        flag += 1

            ch = str(vec[i] + flag)
            while ch in res:
                flag += 1
                ch = str(vec[i] + flag)
            res += ch
        return res


A = Solution()
for i in range(1,25):
    print A.getPermutation(3,i)
    pass
print A.getPermutation(9,54493)
print A.getPermutation(9,54494)
print A.getPermutation(9,54495)

#print 8*7*6*5*4*3*2*2