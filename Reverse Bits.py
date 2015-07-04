class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            temp = n&1
            res =  (res << 1) + temp
            n >>= 1
        return res

A = Solution()
print A.reverseBits(43261596)
print A.reverseBits(0)
print A.reverseBits((1<<32) -1)