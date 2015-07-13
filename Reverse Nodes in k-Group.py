#coding=utf-8
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    # 我看我以前用C++写的，用堆栈写的，也是容易的很~
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        iter = dummy
        temp = dummy.next
        dummy.next = None
        if not head or not k:
            return head
        while 1:
            head = temp
            i = 0
            while temp and i < k:
                i += 1
                temp = temp.next
            #print i,"!"
            if i < k:
                iter.next = head
                break
            temp = head
            tail = temp.next
            while i > 0:
                foo = temp.next
                temp.next = iter.next
                iter.next = temp
                temp = foo
                i -= 1
            iter = head
        return dummy.next

A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
x = A.reverseKGroup(None,2)
while x:
    print x.val
    x = x.next