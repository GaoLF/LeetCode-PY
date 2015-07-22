#coding=utf-8
#---------------------------------------------------------------------------------
#---------------------------------需重点关注！！！！！！------------------------------
#---------------------------------------------------------------------------------
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    # 用我的C++的递归方法携程python，会超时
    # 别人的动态规划方法，但还没有细看
    def isMatch(self, s, p):
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        print dp
        return dp[-1][-1]
    """
    def isMatch(self, s, p):
        i = j = 0
        while j < len(p):
            if j + 1 < len(p) and p[j + 1] == '*':
                if j + 2 <= len(p) and self.isMatch(s[i:],p[j + 2:]):
                    return True
                if i >= len(s) or (p[j] != '.' and s[i] != p[j]):
                    return False
            else:
                if i >= len(s) or (p[j] != '.' and s[i] != p[j]):
                    return False
                j += 1
            i += 1

        if i >= len(s):
            return True
        else:
            return False
            """

A = Solution()
print A.isMatch("aabbc","aab*c")

print A.isMatch("aa","a")
print A.isMatch("aa","aa")
print A.isMatch("aaa","aa")
print A.isMatch("aa", "a*")
print A.isMatch("aa", ".*")
print A.isMatch("ab", ".*")
print A.isMatch("aab", "c*a*b")