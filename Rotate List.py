# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):

        lens = 0
        temp = head
        while temp:
            lens += 1
            temp = temp.next
        k = k % lens
        x = lens - k
        if not head or not k:
            return head
        temp = head
        for j in range(x - 1):
            temp = temp.next
        foo = temp.next
        temp.next = None
        temp = foo
        while temp.next:
            temp = temp.next
        temp.next = head
        return foo

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
x = A.rotateRight(a,5)
while x:
    print x.val
    x = x.next



