class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = s.lower()
        vec = [i for i in s]
        i = len(s) - 1
        while i >= 0:
            if not vec[i].isalpha() and not vec[i].isdigit():
                del(vec[i])
            i -= 1
        if vec[:] == vec[::-1]:
            return True
        else:
            return False


A = Solution()
print A.isPalindrome("A man, a plan, a canal: Panama")
print A.isPalindrome("race a car")
print A.isPalindrome("1a2")
print A.isPalindrome("dad  ")