#coding=utf-8
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    # 我想实现遍插遍做，但是发现难度很大，别人的算法，非常简便
    # 然后注意这个sorted函数，值得注意！
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out

def p(s):
    for i in s:
        print i.start,i.end
    print 'end'

A = Solution()
a = Interval(7,9)
b = Interval(10,11)
c = Interval(5,7)
d = Interval(3,4)
p(A.merge([a,b,c,d]))