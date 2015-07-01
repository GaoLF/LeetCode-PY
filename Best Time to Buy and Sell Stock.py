import sys
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        res = 0
        if not prices:
            return 0
        min_v = prices[0]
        for num in prices:
            res = max(res,num - min_v)
            if min_v > num:
                min_v = num
        return res

A = Solution()
print A.maxProfit([1])
print A.maxProfit([8,3,2,5,6,7,4])