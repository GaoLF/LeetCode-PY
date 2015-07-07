# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        dummy = ListNode(1<<31)
        dummy.next = head
        temp = dummy
        while temp:
            
