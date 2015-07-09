#coding=utf-8
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    # 刚才其实我也想到了，这个就是得s map t,而且t map s
    # 第一遍我只map了一个方向，所以是错的
    def isIsomorphic(self, s, t):
        size = len(s)
        map1 = {}
        map2 = {}
        if len(t) != size:
            return False
        for i in range(size):
            ch1 = s[i]
            ch2 = t[i]
            if ch1 in map1 and ch2 in map2:
                if ch2 != map1[ch1] or ch1 != map2[ch2]:
                    return False
            elif ch1 not in map1 and ch2 not in map2:
                map1[ch1] = ch2
                map2[ch2] = ch1
            else:
                return False
        return True

A = Solution()
print A.isIsomorphic("ab", "aa")
print A.isIsomorphic("foo", "bar")
print A.isIsomorphic("paper", "title")
print A.isIsomorphic("egg", "add")
