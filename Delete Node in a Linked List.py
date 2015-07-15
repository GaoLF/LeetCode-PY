# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
            node.val = node.next.val
            node.next = node.next.next


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
A.deleteNode(a)
while a:
    print a.val
    a = a.next