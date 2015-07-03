#coding=utf-8
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    # 这个题目已经做得很烂了吧
    # 一个快节点每次跳两步，一个满节点每次跳一步
    # 第一次相遇的地方作为起点，与head同时进行往后走，一次一步
    # 第一次相遇的节点就是最后的结果，环的起点
    def detectCycle(self, head):
        fast = slow = None
        if head:
            slow = head.next
            if slow:
                fast = head.next.next
        while head and slow and fast and slow != fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
    #    if not slow or not fast:
    #        return None
        while fast and head != fast:
            head = head.next
            fast = fast.next
        return fast

A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = a
print A.detectCycle(a).val
#print A.detectCycle(b).val