class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        res = []
        if root:
            if root.left:
                res += self.postorderTraversal(root.left)
            if root.right:
                res += self.postorderTraversal(root.right)
            res.append(root.val)
        return res

A = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
a.right = c
b.left = d

print A.postorderTraversal(a)
print A.postorderTraversal(None)