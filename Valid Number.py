class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        vec = []
        x = i = j = 0
        while i < len(s):
            if s[i:i+1]!=' ':
                break
            i += 1
        j = len(s) - 1
        while j >= i:
            if s[j:j+1] != ' ':
                break
            j -= 1
        while i <= j:
            if s[i:i+1] == 'e':
                x = len(vec)
            vec.append(s[i:i+1])
            i += 1
        j = x
        #print vec
        if j != 0:
            vec1 = vec[0:j]
            vec2 = vec[j+1:len(s)]
           # print j,vec1,vec2
            if not (vec1 and vec2):
                return False
            return bool(self.check(vec1) and self.check2(vec2))
        return self.check(vec)

    def check(self,vec):
        #print vec
        if not vec:
            return False
        if vec[0] == '-' or vec[0] == '+':
            del(vec[0])
        i = 0
        while i < len(vec):
            if vec[i] == '.':
                break
            i += 1
        if i < len(vec) and vec[i] == '.':
            del(vec[i])
        if not vec:
            return False
        for num in vec:
            if not num.isdigit():
                return False
        return True

    def check2(self,vec):
       # print vec
        if not vec:
            return False
        if vec[0] == '-' or vec[0] == '+':
            del(vec[0])
        if not vec:
            return False
        for num in vec:
            if not num.isdigit():
                return False
        return True


A = Solution()

print A.isNumber(" 277707e26")
"""
print A.isNumber("3")
print A.isNumber("0.1 ")
print A.isNumber("abc")
print A.isNumber("2e10")
print A.isNumber("2e10")
print A.isNumber("2.e.10")
print A.isNumber("-2.e-.10")
print A.isNumber("-.e-.10")
print A.isNumber("-2.e-2.")
print A.isNumber("e-2.")
print A.isNumber("32e")
print A.isNumber(".1")
print A.isNumber(". 1")
print A.isNumber("6e6.5")
"""
"""
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
"""