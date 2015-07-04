# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.i = -1
        self.nextlist = []
        #if not root:
        #    return
        #self.nextlist.append(root.val)
        self.init_List(root)

    def init_List(self,root):
        if not root:
            return
        if root.left:
            self.init_List(root.left)
        self.nextlist.append(root.val)
        if root.right:
            self.init_List(root.right)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.i + 1 < len(self.nextlist):
            return True
        else:
            return False

    # @return an integer, the next smallest number
    def next(self):
        self.i += 1
        return self.nextlist[self.i]





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
#                      a(1)
#               b(2)           c(3)
#        d(4)       f(6)             e(5)
#                 g(7)
#               h(8)
# Your BSTIterator will be called like this:
i, v = BSTIterator(b), []
while i.hasNext(): v.append(i.next())
print v