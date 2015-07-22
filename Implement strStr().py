#coding=utf-8
class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    # 这个题可以用KMP吧
    # 但是解法却不需要用，只需要用优化的暴力搜索
    # 抽空还是应该熟悉一下KMP算法寻找子串
    def strStr(self, haystack, needle):
        sizeh = len(haystack)
        sizen = len(needle)
        for i in xrange(0,sizeh - sizen + 1):
            for j in xrange(sizen):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1

A = Solution()
print A.strStr("abcdef",'')
print A.strStr("abcdef",'ced')