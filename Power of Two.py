class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        for i in range(32):
            if n == (1<<i):
                return True
        return False

A = Solution()
print A.isPowerOfTwo(0)
print A.isPowerOfTwo(1)
print A.isPowerOfTwo(2)
print A.isPowerOfTwo(3)
print A.isPowerOfTwo(128)
print A.isPowerOfTwo(1024)
print A.isPowerOfTwo(56)
print A.isPowerOfTwo(65)