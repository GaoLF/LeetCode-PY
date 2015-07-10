#coding=utf-8
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    # 这个题之前刚用了C++写的，也是用笨方法解
    # 但是我看时间的排序居然还不错
    # 这个方法其实并不笨，刚才我直接用笨方法写，但是其实这里边也有一个巧妙点，就是这个个位置
    def maxProfit(self, prices):
        size = len(prices)
        res = 0
        for i in range(1,size):
            if prices[i] > prices[i-1]:#判断后边的值比前边一个值要大才行，不然一直变小，没有计算的必要
                left = self.compute(prices,0,i)
                right = self.compute(prices,i,size-1)
                res = max(left + right, res)
        return res

    def compute(self,prices,begin,end):
        if begin >= end:
            return 0
        res = 0
        max_v = prices[end]
        for i in range(end - 1,begin-1,-1):
            if prices[i] > max_v:
                max_v = prices[i]
            else:
                res = max(res,max_v - prices[i])
        return res

A = Solution()
print A.maxProfit([1,2,3,1,5,6,7])
print A.maxProfit([1,2])
print A.maxProfit([])