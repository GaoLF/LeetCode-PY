#coding=utf-8
# 我是用两个栈来实现队列，压栈压到P中，出队列，从q中出，如果q中空了，把p里的全部压到q中
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.p = stack()
        self.q = stack()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.p.push(x)

    # @return nothing
    def pop(self):
        if self.q.isempty():
            while not self.p.isempty():
                self.q.push(self.p.top())
                self.p.pop()
        self.q.pop()

    # @return an integer
    def peek(self):
        if self.q.isempty():
            while not self.p.isempty():
                self.q.push(self.p.top())
                self.p.pop()
        return self.q.top()

    # @return an boolean
    def empty(self):
        return self.p.isempty() and self.q.isempty()

class stack:
    def __init__(self):
        self.s = []
    def push(self,x):
        self.s.append(x)
    def pop(self):
        del(self.s[len(self.s)-1])
    def isempty(self):
        return bool(not len(self.s))
    def top(self):
        return self.s[len(self.s)-1]


A = Queue()
A.push(1)
print A.peek()
A.push(2)
print A.peek()
A.pop()
print A.peek()
print A.empty()
A.pop()
print A.empty()
A.push(3)
A.push(4)
A.push(5)