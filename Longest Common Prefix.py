#coding=utf-8
class Solution:
    # @param {string[]} strs
    # @return {string}
    # 真的应该睁开狗眼仔细看看人家让你返回啥，又错误提交一次，干
    # []的时候返回""，而不是[]，笨蛋！
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        return self.solve(strs,0,len(strs)-1)

    def solve(self,s,begin,end):
        if begin >= end:
            return s[begin]
        s1 = self.solve(s,begin,(begin+end)/2)
        s2 = self.solve(s,(begin+end)/2+1,end)
        return self.merge(s1,s2)


    def merge(self,s1,s2):
        for i in range(len(s1)):
            if i >= len(s2):
                return s2
            if s1[i] != s2[i]:
                return s1[0:i]
        return s1

A = Solution()
print A.longestCommonPrefix(["av","a"])