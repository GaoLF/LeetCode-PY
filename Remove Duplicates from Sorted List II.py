# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        dummy = ListNode(1<<31)
        dummy.next = head
        temp = dummy
        while temp and temp.next:
            ch = temp.next.val
            node = temp.next.next
            while node and node.val == ch:
                node = node.next
            if node != temp.next.next:
                temp.next = node
            else:
                temp = temp.next
        return dummy.next

A = Solution()
a = ListNode(2)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(4)
f = ListNode(4)
a.next,b.next,c.next, = b,c,d,
d.next,e.next = e,f
x = A.deleteDuplicates(a)
while x:
    print x.val
    x = x.next
