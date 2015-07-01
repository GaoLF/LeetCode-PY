class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        res = ["()"]
        if not n:
            return None
        for i in range(0,n-1):
            len_v = len(res)
            list = []
            for j in range(0,len_v):
                len_str = len(res[j])
                for m in range(0,len_str):
                    temp = res[j][0:m] + '()' + res[j][m:len_str]
                    if temp not in list:
                        list.append(temp)
            res = list
        return res


A = Solution()
print A.generateParenthesis(1)
print A.generateParenthesis(2)
print A.generateParenthesis(3)
print A.generateParenthesis(4)