# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    #����ط��и�ע��ĵط����ҳ��԰�resд����ĳ�Ա������Ȼ���ֲ���ͨ�������ܲ���case����ͬһ������в���
    #C++�оͲ��������������
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