class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if len(s)%2:
            size = len(s)/2
        else:
            size = len(s)/2 - 1
        print size,len(s)
        for i in range(size,-1,-1):
           # print 2*i+1,size
            #if s[:i]==s[i:2*i] or s[:i+1] == s[i+1:2*i+1]:
            if 2 * i + 1 < len(s):
                print "!"
                for j in range(i + 1):
                    if s[j] != s[2*i + 1 - j]:
                        break
                else:
                    return s[:2*i+1:-1] + s
            for j in range(i):
                if s[j] != s[2*i - j]:
                    break
            else:
                return s[:2*i:-1] + s


A = Solution()
print A.shortestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#print A.shortestPalindrome("aaacecaaa")
#print A.shortestPalindrome("abcd")
#print A.shortestPalindrome("")
#print A.shortestPalindrome("abcba")
#print A.shortestPalindrome("aaaaaaaaaa")