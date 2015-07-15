# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if not head:
            return head
        temp = head
        vec = []
        i = size = 0
        while temp:
            temp = temp.next
            size += 1
        temp = head
        while temp:
            if i > size/2:
                vec.append(temp)
            if i == size/2:
                mid = 0
                mid = temp
            temp = temp.next
            i += 1
        mid.next = None

        temp = head
        while vec:
            node = temp.next
            temp.next = vec[-1]
            vec[-1].next = node
            temp = node
            del(vec[-1])

A = Solution()
a = ListNode(1)
b = ListNode(4)
c = ListNode(2)
d = ListNode(5)
e = ListNode(3)
a.next = b
b.next = c
#c.next = d
#d.next = e
A.reorderList(a)
x = a
while x:
    print x.val
    x = x.next


