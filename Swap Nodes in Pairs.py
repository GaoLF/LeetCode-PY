# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head:
            return head
        iter = head
        temp = head
        while iter and iter.next:
            temp_node = temp.next
            if temp == head:
                temp_node = iter.next.next
                head = head.next
                head.next = iter
                head.next.next = temp_node
                iter = temp_node
            else:
                temp_node = iter.next.next
                temp.next = iter.next
                iter.next.next = iter
                iter.next = temp_node
                temp = iter
                iter = iter.next
        return head

A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
#a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
x = A.swapPairs(a)
while x:
    print x.val
    x = x.next




