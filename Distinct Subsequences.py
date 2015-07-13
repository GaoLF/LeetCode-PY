#coding=utf-8
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    # 终于做对了，就是从前边往后边加
    # 如果当前位两个序列的字母相同，匹配到当前的数目等于s和t分别前一个字母的数目之和
    # 只要想到用dp动态规划，求t的每一位的结果，用整个s与一位一位的t作比较
    def numDistinct(self, s, t):
        if len(s)<len(t) or not len(s):
            return 0
        vec = [0 for i in range(len(s)+1)]
        for m in range(len(t)):
            temp = [0 for i in range(len(s)+1)]
            for i in range(len(s)):
                if s[i] == t[m]:
                    if m == 0:
                        temp[i+1] = temp[i] + 1
                    else:
                        temp[i+1] = temp[i] + vec[i]
                else:
                    if i:
                        temp[i+1] = temp[i]
            vec = temp
        return temp[len(s)]

A = Solution()
print A.numDistinct("rabbbit","rabit")
print A.numDistinct("aabacaacbca","abc")
print A.numDistinct("","abc")
print A.numDistinct("eee","eee")