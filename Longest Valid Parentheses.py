#coding=utf-8
class Solution:
    # @param {string} s
    # @return {integer}
    # 必须得想点有用的方法，正常遍历，总会遇到右边多左括号的问题
    # 这里采用的方法是把所有匹配的括号的序号删掉，然后留下的全是不匹配的系数，然后计算他们之间的差
    def longestValidParentheses(self, s):
        vec = []
        res = 0
        for i in xrange(len(s)):
         #   print vec
            if s[i] == '(':
                vec.append(i)
            else:
                if not vec or s[vec[-1]] == ')':
                    vec.append(i)
                else:
                    del(vec[-1])
        #print vec
        for i in xrange(1,len(vec)):
            res = max(res,vec[i]- vec[i-1]-1)
        return len(s) if not vec else max(res,vec[0],len(s)-vec[-1]-1)

A = Solution()
print A.longestValidParentheses("()")
print A.longestValidParentheses("()(")
print A.longestValidParentheses("()())))")
print A.longestValidParentheses("()((((()")
print A.longestValidParentheses("(((()()()((")
print A.longestValidParentheses("()((((()")
#print A.longestValidParentheses("(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()())))(())()())((((()())((())))((()))()())))()(()()()(()((()))()()()))()()()(()()((((())()(((()(((())((()))()((()(()))()())))))))))())()())(()()))((()()()()())))((()()((((()()))))(())())()()))))(())()(()))((((((()))(()()()()(())(()((()))(()(())(((()()))(()((((()((((()((((())(())))()(())))()))(()((((((((())()()((())((()())()))))())())()(((((()()(((((())()((()(((()))(()(()))(()(()())))())(()((((()((()(((((()()))((()(()((())()))))(()(()())((()((()((((())))(()())()))()())())()))))(())))(())()((())(()(()))))()())(((()(()(((((((((()(()()())))((()((()())())())(((((()(()))))()))()))))()())()(()(())))(()))))(()))(((()))))())))))(((())((())((((()((()))((())))()))(((()))())()))()()()((()()(()())(()))()()((()())))))())(()())(((())))))())(())()))()())())(()(()((())((()(()((())(()()()(()((()(((()(())()(((())))))()())))))(()((((()(()()))(((())(()))(()()))))(())()((()))()))()()))()((())(()())())())(()))(()()(())()(()((((()())(((())(()()())())(()()))())))(()((())(()()))))(()))((()()((((()())(()()))()())()())))()(()((((())())()(())()))()()(()(()))))))(((()()((()))(()((((()()((())))())())))()())))())))((())()()()))()((()((()))()()())))(())())(()(()(()(()))())()))(())((())()())(((()()(((())(()()))(()())(())))()))(((()()()())))())))(((()))())())())))(((()))()())())())))))()()()()(())))(()())))(()()())))()((((()()()((((()))()())))(()))()))))(()())()))(((((())()((())()))(()())()()()())()(((()(()(())))))(()(((()()))((((()()))()))(((())(()(()))()(())))()()(()))))()))))()())))()))((((((((()()())((()(()()()(((())())())))()()(())(())))()())()())))((()))((((())()()))(())(((())(()()(((((()()((()()(((()(()()(((())()))))()(()())(()((((()()())(((()))(())((())()))))())))))(()()()())))()))(())((()())()())()()))(())))((()))()()((()())()()))(()()(())()())(())))((()(((())))()))))((((()))((())())())()(())(()))((((((())()()(((((()))()())(((()(()(())()((()())))(((())(()(())))))(()(()(((()))(())((((())))((())((((((((()(((((()(())))((((((())(()((((()(())()()((())())())((((((((()))))(((())()))()()))(())(())()()())(()()((())(()))())(((())(()((())(())(())))))(()(()(()()(((()()()))())(()))(())())()(((()((())((()())()(((((()()(()))))(((())()()))(()(()(()(()((())))))))(())())()))()(()(()))))()()((((())()())(((())(()))((()())(()((())()()(())((((())))))(())())())(())(()()(()()))(((()((((())(((())))))(()()()()(((()((((())(()))((())()))()(((((((()(()())))((()()(()()((())()))()(())))((()()((((()()()))((())()))((())(((()(()()()(((()((())((())()())())))((()))))))))))(())()()(((()()())))(((()))(()))))(((()(()())(()))(())((()))(((()(()()(((((((()())((((()))((((()(()())())()(((()(()((()))))))))))()()(((()()((((((((((())))))((((())())((()(((()())()))()()(((((())(()())())(((()((())((((((())(((())(((()(()(((((((()(())()())(()))))(()(((()))))))()))(((())))(()(()())()))(()()(()(()((()())()(())((()()((()()()(()(()()))(((((())()(()())()((()())()))(((((()((())()((()((((()(((())())(()()(())()(())(()(())))))(()())((()((()()()())(()))(()))))))(()((())(())((())()())()()))(()((()))(()()))()())(())(()()(()))((())()((())((((((())()(()()(((((())(()())())())()()(()())))))()))()((())((((((()())((()))))))((()(()()(((((((())))))))((()))(())(((()(()(())()()()()(()(())()))))))())()))()(((((()(())(((()))((()))()))()()(()(()((())(()))))()())((()())))))))(()()(()()))()((()(())()((())(()()))())((()())())()()))))((((()()()))())(())()())))()))()))))()))((()(()())()))()))(((()()()()())))())()))((()()())((()())))(((()((()()())(())))()(())(()(()(())(()(((((()()()(((())()())(()((()())(()(((()(())((((()())()(())))(((((((()))))())())))(()))()()(((()())(()))()())(())()))()((())()((())((()((())()())(()()))(((((()()()((((((((()(()((()()((((((()())))((((((())))())(()(()((((()(()())())()()))()((())())(()((((()(((()())((())))))(()())(()()()(()))()())()()))((()((()())(())()()()((())()()))))())()))())))(()))(()))()))((())()((()((()))))))())(((()))))))()(((()((())))((()())())()))((()(()(()(()))((()()))())))(()())))())(()))(())(())))))()(())(()()))()))((())))(()))(()))))(())()())(()(()))())(()(())(())))(()))())(()())))())(()())((()))()()((()(()()()(((((()((()((())(()())(())))()))))))(((())())))()((((()))()((()))())()))()))(()(()((()()())()()(((()))())))))()((((()()))))()))())))()())))(((((()(())))())(((()))((()))(((()(())())()((()(((()))()())))))((((()))()(()((((((()(()()()())(())((()))()(()()))))))()(((())))(())()())))))((()))(())()))))(()(((()()((())(()))))(((((()))))())))()(())(()(()))()))()))(()((())(()((()())()(((()))))())(())()(())))((())(()(((()))(((((()))(()))())))(()((((((())()((((())())()))((())))))())(()(())())))))()()(((())()())))))()))()())))()(())())(())()()()(((())))(())(((()))(()(((()()))())((()))(((()()()()())()()))(()))))()()))))(((()()))))()()(()()))()()()())())()((())(((()())(((())(()((()(((()(()())()()()(()((())(()()(()()()))))))()((()))))()(()))()))(())()()())))()()(((()))((()()(((()())))((()()())((())))))()())()((())))())(()())()()()()((())((()()())((()()))())(())())()(()(((()))())(()))))(()()))(())))))))()())()((()())()()))()())))((()()(()())()(()))((())()))(((())))())))(((()()())())(")