#coding=utf-8
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
# 这个题我直接用的之前的插入排序，条件符合，但是测试case是一个很长的而且重复很多的list
# 这个题应该用归并的方法
# 没想到写了这么多代码，还是在很小的错误 上失误，查了很久，要细心啊！
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next:
            return head
        #self.p(head)
        l1 = head
        temp = head
        len = 0
        while temp:
            temp = temp.next
            len += 1
        i = 1
        temp = head
        while i < (len/2):
            i += 1
            temp = temp.next
        l2 = temp.next
        temp.next = None
        #self.p(l1)
        #self.p(l2)
        #print
        left = self.sortList(l1)
        right = self.sortList(l2)
        #self.p(self.merge(l1,l2))
        #self.p(left)
        #self.p(right)
        #print self.merge(l1,l2)
        #print
        return self.merge(left,right)

    def merge(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1<<31)
        dummy.next = l1
        temp = dummy

        #print
        while l2:
            if not temp.next:
                temp.next = l2
                break
            if (l2.val < temp.next.val):
                #self.p(l1)
                a = l2.next
                l2.next = temp.next
                temp.next = l2
                temp = l2
                l2 = a
            #    self.p(dummy.next)
            else:
                temp = temp.next
        #self.p(dummy)
        return dummy.next

    def p(self,x):
        while x:
            print x.val,
            x = x.next
        print None

A = Solution()
a = ListNode(1)
b = ListNode(4)
c = ListNode(2)
d = ListNode(5)
e = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = e
x = A.sortList(a)
while x:
    print x.val
    x = x.next
