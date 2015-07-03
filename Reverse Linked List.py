# Definition for singly-linked list.
#coding=utf-8
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    # 一定注意最后一个节点要指向前一个节点，因为在遍历的时候后边的节点要和中间的节点断开
    # 一定要注意第一个节点要指向None，不然前两个节点会陷入死循环
    def reverseList(self, head):
        if not head or not head.next:
            return head
        temp = head
        next_node = head.next
        while next_node and next_node.next:
            temp_node = next_node.next
            next_node.next = temp
            temp = next_node
            next_node = temp_node
        next_node.next = temp
        head.next = None
        return next_node

    def printlist(self,root):
        while root:
            print root.val,"->",
            root = root.next

A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
#b.next = c
c.next = d
d.next = e
x = A.reverseList(a)
A.printlist(x)
