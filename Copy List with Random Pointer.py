# Definition for singly-linked list with a random pointer.
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        dic = {}
        if not head:
            return None
        new_head = RandomListNode(head.label)
        if head.random:
            node = RandomListNode(head.random.label)
            new_head.random = node
            dic[head.random] = node
        temp_h = head.next
        temp_n = new_head
        while temp_h:
            if temp_h in dic:
                temp_n.next = dic[temp_h]
            else:
                new_node = RandomListNode(temp_h.label)
                temp_n.next = new_node
            temp_n = temp_n.next
            if temp_h.random:
                if temp_h.random in dic:
                    temp_n.random = dic[temp_h.random]
                else:
                    node = RandomListNode(temp_h.random.label)
                    temp_n.random = node
                    dic[temp_h.random] = node
            temp_h = temp_h.next
        return new_head

def p(x):
    while x:
        print x.label,
        if x.random:
            print x.random.label
        else:
            print "none"
        x = x.next

A = Solution()
a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)
a.next = b
b.next = c
a.random = c
b.random = a
p(a)
x = A.copyRandomList(a)
p(x)
