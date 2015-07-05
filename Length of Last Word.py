#coding=utf-8
class Solution:
    # @param {string} s
    # @return {integer}
    # 在leetcode上用for循环，居然for循环里的i，j不能再块外边用
    # 鉴于循环外边不能用i，j，我用一个a，b分别代替，也没有做更多的优化
    def lengthOfLastWord(self, s):
        if not len(s):
            return 0
        a = len(s) -1
        for i in range(len(s)-1,-1,-1):
            a = i
            if s[i] != ' ':
                break
        b = a
        for j in range(b,-1,-1):
            b = j
            if s[j] == ' ':
                break
        if s[b]!=' ':
            b -= 1
        return a - b

A = Solution()
print A.lengthOfLastWord("Hello World")
print A.lengthOfLastWord("Hello World  ")
print A.lengthOfLastWord("")
print A.lengthOfLastWord("Hel      ")