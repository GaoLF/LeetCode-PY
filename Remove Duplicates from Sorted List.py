# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head



A = Solution()
a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = e
#e.next = f
a = A.deleteDuplicates(a)
a = A.deleteDuplicates(None)
while a:
    print a.val
    a = a.next

#print a.next.val
