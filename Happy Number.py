class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        loop_set = set([])
        while n != 1:
            sum_v = 0
            while n:
                temp = n%10
                n = n/10
                sum_v += temp**2
            if sum_v in loop_set:
                return False
            loop_set.add(sum_v)
            n = sum_v
        return True

A = Solution()
print A.isHappy(0)
print A.isHappy(1)
print A.isHappy(19)
print A.isHappy(33)