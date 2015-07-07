# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        vir = ListNode(1<<31)
        vir.next = head
        iter = vir
        while iter:
            if iter.next and iter.next.val == val:
                temp = iter.next.next
                iter.next = temp
                #iter = iter.next
            else:
                iter = iter.next
        return vir.next

A = Solution()
a = ListNode(1)
b = ListNode(1)
c = ListNode(6)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)
g = ListNode(6)
a.next,b.next,c.next,d.next,e.next,f.next = b,c,d,e,f,g
x = A.removeElements(a,6)
while x:
    print x.val
    x = x.next

