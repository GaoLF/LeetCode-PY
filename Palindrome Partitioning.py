class Solution:
    # @param {string} s
    # @return {string[][]}python
    def partition(self, s):
        size = len(s)
        if not s:
            return []
        res = [[] for i in range(size+1)]
        for i in range(size):
            for j in range(i+1):
                temp_s = s[j:i+1]
                if temp_s == temp_s[::-1]:
                 #   print i,j,temp_s
                    if not j:
                        res[i].append([s[j:i+1]])
                    else:
                        for iter in res[j-1]:
                            temp = iter[:]
                            temp.append(temp_s)

                            res[i].append(temp)

        return res[size-1]

A = Solution()
print A.partition("abccbad")
#x = "abc"
#print x[0:0:-1]
print A.partition("a")
print A.partition("")