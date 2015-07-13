# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        temp = dummy
        while l1 and l2:
            sum_v = l1.val + l2.val + carry
            carry = (sum_v)/10
            sum_v %= 10
            temp.next = ListNode(sum_v)
            temp = temp.next
            l1,l2 = l1.next,l2.next
        if not l1 and not l2:
            if carry:
                temp.next = ListNode(1)
        elif l2:
            l1 = l2
        while l1:
            sum_v = l1.val + carry
            carry = (sum_v)/10
            #print sum_v
            sum_v %= 10
            #print sum_v
            temp.next = ListNode(sum_v)
            temp = temp.next
            l1 = l1.next
        if carry:
            temp.next = ListNode(1)
        return dummy.next

A = Solution()
a = ListNode(1)
b = ListNode(4)
c = ListNode(9)
d = ListNode(5)
e = ListNode(9)
a.next = b
#b.next = c
c.next = d
d.next = e
x = A.addTwoNumbers(a,c)
while x:
    print x.val
    x = x.next