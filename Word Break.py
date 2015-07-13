#coding=utf-8
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    # 一开始用我的方法过不去，后来想到可以用一个flag list来表示已经算过的不行的，然后就可以避免重复计算
    # 我的方法在排名上居然很靠前
    def wordBreak(self, s, wordDict):
        if not wordDict:
            return False
        size = [len(i) for i in wordDict]
        flag = [0 for i in range(len(s) + 1)]
        max_size = max(size)
        min_size = min(size)
        return self.solve(s,wordDict,max_size,min_size,flag)
        #print max_size

    def solve(self,s,dic,maxs,mins,flag):
        size = len(s)
        if flag[size]:
            return False
        if size < mins:
            return False
        if size <= maxs and s in dic:
            return True
        for i in range(mins,maxs+1):
            if i <= len(s):
                temp = s[:i]
                if temp in dic:
                    if self.solve(s[i:],dic,maxs,mins,flag):
                        return True
        flag[size] = 1
        return False

A = Solution()
print A.wordBreak("abcdefg",["abc",'acde'])
print A.wordBreak("abcdefg",["ab",'cd','efg'])
print A.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])