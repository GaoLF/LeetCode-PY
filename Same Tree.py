# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    
    #python��True��False������''��""��0��()��[]��{}��NoneΪFalse֮�⣬�����Ķ���True
    #����ط�дreturn 1 0��Ȼ����
    def isSameTree(self, p, q):
        if p and q:
            if p.val == q.val:
                return (self.isSameTree(p.left,q.left) & self.isSameTree(p.right,q.right))
            else:
                return False
        elif p == None and q == None:
            return True
        else:
            return False