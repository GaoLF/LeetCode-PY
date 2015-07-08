#coding=utf-8
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    # 设立两个指针，一个是从0开始，一个是从k开始，同时往后走，当从k开始走的到头了，从零开始的就是倒数第k个
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        kth = dummy
        i = 0
        if not n:
            return head
        while kth.next:
            if i < n:
                kth = kth.next
                i += 1
            else:
                kth = kth.next
                temp = temp.next
        temp.next = temp.next.next
        return dummy.next

A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next,b.next,c.next = b,c,d
x=A.removeNthFromEnd(a,0)
while x:
    print x.val
    x = x.next