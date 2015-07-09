#coding=utf-8
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    # 我是把所有大于等于x的节点串在一起，然后用小于的最后一个节点指向大于等于的第一个节点
    # 需要注意的是，大于的节点最后一定要指向None，不然就死循环了
    def partition(self, head, x):
        dummy = ListNode(0)
        dummy.next = head
        rightnode = ListNode(0)
        temp = dummy
        temp_r = rightnode
        while temp.next:
            #print temp.val
            if temp.next.val >= x:
                temp_r.next = temp.next
                temp_r = temp_r.next
                temp.next = temp.next.next
            else:
                temp = temp.next
        temp_r.next = None
        temp.next = rightnode.next
        #return rightnode.next
        return dummy.next

A = Solution()
a = ListNode(3)
b = ListNode(2)
c = ListNode(5)
d = ListNode(3)
e = ListNode(2)
f = ListNode(1)
a.next,b.next,c.next, = b,c,d,
d.next,e.next = e,f
x = A.partition(None,3)
while x:
    print x.val
    x = x.next
