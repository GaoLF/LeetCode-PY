#coding=utf-8
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
#********************************************************
#************************这个题***************************
#******************和下一个题是一个系列的********************
#**********************值得再看看**************************
#********************************************************
class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    # 别人的三种算法，自己的猪脑子做半天不行
    # 但是我是试图在循环内完成，而不是借助于一个额外的数组
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left, right = [], []
        for i in intervals:
            if i.end < s:
                left += i,
            elif i.start > e:
                right += i,
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right

    """
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
        return left + [Interval(s, e)] + right

    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        parts = merge, left, right = [], [], []
        for i in intervals:
            parts[(i.end < s) - (i.start > e)].append(i)
        if merge:
            s = min(s, merge[0].start)
            e = max(e, merge[-1].end)
        return left + [Interval(s, e)] + right
    """

def p(s):
    for i in s:
        print i.start,i.end
    print 'end'

A = Solution()
a = Interval(1,5)
b = Interval(-2,-1)
c = Interval(9,10)
d = Interval(15,17)
p( A.insert([a],Interval(2,3) ) )