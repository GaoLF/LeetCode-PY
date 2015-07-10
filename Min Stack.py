class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.vec = []
        self.size = 0
        self.minvec = []
        self.minsize = 0
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.vec.append(x)
        self.size += 1
        if not self.minsize or x < self.minvec[self.minsize-1]:
            self.minvec.append(x)
            self.minsize += 1

    # @return nothing
    def pop(self):
        temp = self.vec[self.size-1]
        del(self.vec[self.size-1])
        self.size -= 1
        if temp == self.minvec[self.minsize-1]:
            del self.minvec[self.minsize - 1]
            self.minsize -= 1

    # @return an integer
    def top(self):
        return self.vec[self.size-1]


    # @return an integer
    def getMin(self):
        return self.minvec[self.minsize-1]

A = MinStack()
A.push(3)
print A.top()
print A.getMin()
print
A.push(2)
A.push(4)
A.push(5)
A.push(1)
print A.top()
print A.getMin()
print
A.pop()
print A.top()
print A.getMin()
print
A.pop()
print A.top()
print A.getMin()
print
A.pop()
print A.top()
print A.getMin()
print

