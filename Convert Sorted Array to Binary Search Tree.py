# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        half = len(nums)/2
        root = TreeNode(nums[half])
        root.left = self.sortedArrayToBST(nums[0:half])
        root.right = self.sortedArrayToBST(nums[half+1:len(nums)])
        return root


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


A = Solution()

a = A.sortedArrayToBST([1,2,3,4,5,6])
print A.preorderTraversal(a)
a = A.sortedArrayToBST([2,4,5,6,7])
print A.preorderTraversal(a)
