class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        sign = before = 1
        i = begin = res = 0
        flag = [1]
        size = len(s)
        if not size:
            return 0
        while i < size:
            ch = s[i]
            if ch == '(':
                if not i:
                    pass
                else:
                    for j in xrange(i-1,-1,-1):
                        if s[j] == '+':
                            flag.append(1)
                            break
                        if s[j] == '-':
                            flag.append(-1)
                            break
                before = before * flag[-1]
                sign = before
            elif ch == ')':
                before = before * flag[-1]
                del(flag[-1])
            elif ch == '+':
                sign = before
            elif ch == '-':
                sign = -before
            elif ch.isdigit():
                begin = i
                for i in xrange(begin,size):
                    if not s[i].isdigit():
                        break
                #print begin,i
                if i == size - 1 and s[i].isdigit():
                    i += 1
                num = int(s[begin:i])
                # sign,num,begin,i,s
                res += num*sign
                #print res,num*sign
                i -= 1
            i += 1

        return res

A = Solution()
a = ' 1 + 2- (3 - (4-533+3))'
print A.calculate(a)
print A.calculate("(1)")
print A.calculate('(1+(4+5+2)-3)+(6+8)')


print A.calculate("1-(3+5-2+(3+19-(3-1-4+(9-4-(4-(1+(3)-2)-5)+8-(3-5)-1)-4)-5)-4+3-9)-4-(3+2-5)-10")