class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        flag = [0 for i in range(128)]
        i = 0
        begin = 0
        res = 0
        while i < len(s):
            c = s[i:i+1]
            if flag[ord(c)]:
                res = max(res,i-begin)
                #print
                while s[begin: begin + 1] != c:
                    flag[ord(s[begin])] = 0
                    begin += 1
                begin += 1
            else:
                flag[ord(c)] = 1
            i += 1
        return max(res,len(s) - begin)

A = Solution()
print A.lengthOfLongestSubstring("")
print A.lengthOfLongestSubstring("abcabcbb")
print A.lengthOfLongestSubstring("abbcbba")
print A.lengthOfLongestSubstring("abcdcf")
print A.lengthOfLongestSubstring("abcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghigabcdefghig")
