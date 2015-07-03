# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        res = []
        if not root:
            return res
        #res.append()
        nodes = [root]
        while nodes:
            temp = []
            tempv = []
            for node in nodes:
                tempv.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(tempv)
            nodes = temp
        return res

A = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
a.left = b
a.right = c
b.left = d
c.right = e
b.right = f
f.left = g
g.left = h
print A.levelOrder(None)