class Stack:
    # initialize your data structure here.
    #stack = []
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        #size = len(self.stack)
        del(self.stack[len(self.stack)-1])

    # @return an integer
    def top(self):
        return self.stack[len(self.stack)-1]

    # @return an boolean
    def empty(self):
        return bool(not len(self.stack))

A = Stack()
print A.empty()
A.push(1)
A.pop()
print A.empty()


A.push(1)
A.push(2)
print A.top()
A.push(3)
A.push(4)
print A.top()
A.pop()
print A.top()
A.pop()
print A.top()
print A.empty()
A.pop()
A.pop()
print A.empty()

