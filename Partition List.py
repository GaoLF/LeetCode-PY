# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        vitul = ListNode(0)
        vitul.next = head
        leftnodes = head
        temp = vitul.next
        while temp:
            if temp.val < x:
                