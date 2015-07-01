class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        roman = {'I':1,'X':10,'C':100,'M':1000,'V':5,'L':50,'D':500}
        res = 0
        if not s:
            return None
        for i in range(0,len(s)-1):
            if roman[s[i:i+1]] < roman[s[i+1:i+2]]:
                res -= roman[s[i:i+1]]
            else:
                res += roman[s[i:i+1]]
        res += roman[s[len(s)-1:len(s)]]
        return res

A = Solution()
print A.romanToInt("MDCCCLXXXVIII")
print A.romanToInt("MDCCCXCIX")
print A.romanToInt("IX")
print A.romanToInt("")