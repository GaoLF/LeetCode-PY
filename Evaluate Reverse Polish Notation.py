#coding=utf-8
import math
class Solution:
    # @param {string[]} tokens
    # @return {integer}
    # 这个地方有很多知识点：
    # math函数：math.floo想下取整，math.ceil向上取整
    # round 函数四舍五入取整，这些取整方法都是返回浮点数
    # eval函数，可以直接计算字符串的输出
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t in '+-*/':
                stack[-2] = str(int(eval((stack[-2]+t+stack[-1]))))
                del(stack[-1])
            else:
                stack.append(t+'.')
            """
            if t == '+':
                stack[-2] += stack[-1]
                del(stack[-1])
            elif t == '-':
                stack[-2] -= stack[-1]
                del(stack[-1])
            elif t == '*':
                stack[-2] *= stack[-1]
                del(stack[-1])
            elif t == '/':
                stack[-2] /= stack[-1]
                del(stack[-1])
            else:
                stack.append(float(t))
                """
            #print (stack)
        return int((stack[0]))

A = Solution()
print A.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print A.evalRPN(["4", "13", "5", "/", "+"])
print (-10/float(3)),int(float(-10)/3),int(float(-10/3)),int(float(-10)/float(3))