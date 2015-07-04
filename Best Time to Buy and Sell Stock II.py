class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        res = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

A = Solution()
print A.maxProfit([3,2,1,4,5,3,7])
print A.maxProfit([])
print A.maxProfit([3])