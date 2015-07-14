class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        max_v = 1
        res = ""
        size = len(s)
        if size <= 1:
            return s
        for i in xrange(size):
            if i - max_v >= 1:
                temp = s[i-max_v-1:i+1]
                if temp == temp[::-1]:
                    max_v += 2
                    res = temp
                    continue
            if i - max_v >= 0:
                temp = s[i - max_v:i+1]
                if temp == temp[::-1]:
                    res = temp
                    max_v += 1
        return res

A = Solution()
print A.longestPalindrome("abcdeffedafg")
print A.longestPalindrome("abcbaf")
print A.longestPalindrome("a")
print A.longestPalindrome("")
print A.longestPalindrome("aa")
print A.longestPalindrome("")