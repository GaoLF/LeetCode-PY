class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        width = 1
        x = abs(x)
        while x/width:
            width *= 10
        width /= 10
        while x:
            if x%10 != x/width:
                return False
            x = (x%width)/10
            width /= 100
        return True


A = Solution()
print A.isPalindrome(12345654321)
print A.isPalindrome(0)
print A.isPalindrome(123345654321)
print A.isPalindrome(-2147483648)
print A.isPalindrome(-12345654321)