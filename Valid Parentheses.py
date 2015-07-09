class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        pars = []
        for iter in s:
            size = len(pars)
            if iter == '(' or iter == '[' or iter == '{':
                pars.append(iter)
            elif iter == ']':
                if size > 0 and pars[size - 1] == '[':
                    del(pars[size - 1])
                else:
                    return False
            elif iter == '}':
                if size > 0 and pars[size - 1] == '{':
                    del(pars[size - 1])
                else:
                    return False
            elif iter == ')':
                if size > 0 and pars[size - 1] == '(':
                    del(pars[size - 1])
                else:
                    return False
        return not bool(len(pars))

A = Solution()
print A.isValid("{}")
print A.isValid("{[}()]")

print A.isValid("{[()()]}((")