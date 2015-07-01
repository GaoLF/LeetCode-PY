#coding=utf-8
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    #这个题险些滑铁卢了，最简单的方法应该就是挨个往后走，谁小就连谁
    #有的人还用了一种方法，设立一个起始点，然后所有的点从起始点开始往后加少去一些我的这个起始点的检测
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        res = iter = l1
        while l1 and l2:
            if l1.val <= l2.val:
                if l1 != res:#当前点不是起始点
                    iter.next = l1
                    iter = iter.next
                l1 = l1.next
            else:
                if l1 == res:
                    res = l2
                    iter = l2
                else:
                    iter.next = l2
                    iter = iter.next
                l2 = l2.next
        if l1 or l2:#这个地方是跟别人学的，感觉还不错！
            iter.next = l1 or l2

        return res

A = Solution()
a1 = ListNode(-9)
b1 = ListNode(3)
c1 = ListNode(5)
d1 = ListNode(7)
a1.next = b1
b1.next = c1
c1.next = d1

a2 = ListNode(5)
b2 = ListNode(7)
c2 = ListNode(3)
d2 = ListNode(4)
a2.next = b2
b2.next = c2
c2.next = d2

x = A.mergeTwoLists(a1,a2)
while x:
    print x.val
    x = x.next