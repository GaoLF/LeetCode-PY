# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        return self.merge(lists,0,len(lists)-1)

    def merge(self,lists,begin,end):
        print begin,end
        if begin > end:
            return None
        if begin == end:
            return lists[begin]
        if begin == end - 1:
            return self.merge2list(lists[begin],lists[end])
        left = self.merge(lists,begin,(end-begin)/2+begin)
        right = self.merge(lists,(end-begin)/2+begin+1,end)
        return self.merge2list(left,right)

    def merge2list(self,l1,l2):
        dummy = ListNode(-1<<30)
        temp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        return dummy.next

A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(-1)
d = ListNode(3)
e = ListNode(5)
a.next = b
#b.next = c
c.next = d
d. next = e
x = A.mergeKLists([a,c,c,c,c,a])
while x:
    print x.val
    x = x.next