# Definition for a undirected graph node
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        dic = {}
        vec = [node]
        #vec
        while vec:
            temp = []
            for iter in vec:
                if iter not in dic:
                    clone = UndirectedGraphNode(iter.label)
                    dic[iter] = clone
                for nd in iter.neighbors:
                    if nd not in dic:
                        clnd = UndirectedGraphNode(nd.label)
                        dic[nd] = clnd
                        temp.append(nd)
                    dic[iter].neighbors.append(dic[nd])
                vec = temp
        return dic[node]

A = Solution()
a = UndirectedGraphNode(1)
b = UndirectedGraphNode(2)
c = UndirectedGraphNode(3)
a.neighbors.append(b)
a.neighbors.append(c)
c.neighbors.append(a)

print A.cloneGraph(a).label
print A.cloneGraph(a).neighbors[0].label
print A.cloneGraph(a).neighbors[1].label
print A.cloneGraph(a).neighbors[1].neighbors[0].label
