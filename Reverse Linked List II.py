# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        i = 0
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        temp = []
        while True:
            if i+1 < m:
                i += 1
                node = node.next
            elif i+1 == m:
                begin = node
                while i < n:
                    temp.append(node.next)
                    node = node.next
                    i += 1
                node = node.next
                for j in range(len(temp)):
                    begin.next = temp[len(temp)-j-1]
                    begin = begin.next
                begin.next = node
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
x = A.reverseBetween(a,1,6)
while x:
    print x.val
    x = x.next