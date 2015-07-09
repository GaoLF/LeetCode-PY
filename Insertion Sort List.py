#coding=utf-8
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
# 这个题第一遍规规矩矩的做插入排序，但是居然没有通过，因为给的case是一个1~很大很大的数，
# 也就意味着那是插入排序的最坏情况，每一次遍历需要从第一个节点遍历到最后一个节点
# 改进方法：设立一个左边链表（排好序的list）的end指针，如果待插指针的大小大于end的val值，直接插在end的后边
# 可以节省很多时间，而且，这样导致待插值一定小于左边链表的某个值，循环也可以写的更简单一些
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        dummy = ListNode(-1<<31)
        dummy.next = head
        iter = dummy.next
        while iter:
            temp = iter
            if iter == head:
                iter = iter.next
                head.next = None
                end = head
            else:
                iter = iter.next
                if temp.val >= end.val:
                    temp.next = None
                    end.next = temp
                    end = temp
                else:
                    #从head开始插
                    iter2 = dummy
                    while iter2.next.val < temp.val:
                        iter2 = iter2.next
                    temp.next = iter2.next
                    iter2.next = temp
        return dummy.next

A = Solution()
a = ListNode(1)
b = ListNode(4)
c = ListNode(2)
d = ListNode(5)
e = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = e
x = A.insertionSortList(a)
while x:
    print x.val
    x = x.next

