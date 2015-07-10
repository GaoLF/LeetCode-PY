# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        dummy = ListNode(0)
        dummy.next = head
        len = 0
        temp = head
        while temp:
            len += 1
            temp = temp.next
        temp = dummy.next
        dummy.next = None
        for i in range(len/2):
            foo = temp.next
            bar = dummy.next
            dummy.next = temp
            temp.next = bar
            temp = foo
        l2 = temp
        head = dummy.next
        if len%2:
            temp = temp.next
        #self.p(head)
        #self.p(temp)
        while temp:
            if temp.val != head.val:
                return False
            temp = temp.next
            head = head.next
        return True

    def p(self,x):
        while x:
            print x.val,
            x = x.next
        print

A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(2)
e = ListNode(2)
a.next = b
b.next = c
c.next = d
d.next = e
print A.isPalindrome(a)
#print A.isPalindrome(b)
#print A.isPalindrome(c)
#print A.isPalindrome(e)