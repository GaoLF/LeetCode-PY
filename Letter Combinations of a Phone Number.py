class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        res = temp = []
        dic = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
               '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
               '8':['t','u','v'],'9':['w','x','y','z'],'0':[' ']}
        for num in digits:
            res = []
            if not temp:
                for char in dic[num]:
                    res.append(char)
            else:
                for iter in temp:
                    for char in dic[num]:
                        letters = iter[:]
                        letters += char
                        res.append(letters)
            temp = res
        return res

A = Solution()
print A.letterCombinations("23")
print A.letterCombinations("423")
print A.letterCombinations("70")