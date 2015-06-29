# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        parient_l = [root]
        while parient_l:
            son_l = []
            for node in parient_l:
                if node.left:
                    son_l.append(node.left)
                if node.right:
                    son_l.append(node.right)
            for i in range(0,len(son_l)-1,1):
                son_l[i].next = son_l[i+1]
            parient_l = son_l