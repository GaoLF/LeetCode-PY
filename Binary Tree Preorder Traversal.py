# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    #这个地方有个注意的地方：我尝试把res写成类的成员变量，然后发现不能通过，可能测试case是用同一个类进行测试
    #C++中就不会出现这种问题
    def preorderTraversal(self, root):
        res = []
        if root is None:
            return res
        res.append(root.val)
        if root.left:
            res = res + self.preorderTraversal(root.left)
        if root.right:
            res = res + self.preorderTraversal(root.right)
        return res