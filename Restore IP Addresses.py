#coding=utf-8
class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        res = []
        self.solve(s,0,0,res,"")
        return res
# 几点注意事项：当位数太多或者太少，都不能组成
# 当第一个数是0的时候，只能当0
    def solve(self,s,i,begin,res,string):
        size = len(s)
        if (size - begin) < 1*(4 - i):
           return
        if (size - begin) > 3*(4 - i):
            return
        if i == 3:
            num = int(s[begin:size])
            if num > 255:
                return
            else:
                if s[begin:begin+1] == '0' and begin + 1 < size:
                    return
                res.append(string + s[begin:size])
        else:
            if s[begin:begin+1] == '0':
                #string = string + '0.'
                self.solve(s,i+1,begin+1,res,string + '0.')
                #string = string[0:begin]
            else:
                for j in range(3):
                    if begin + j + 1 < size:
                        num = int(s[begin:begin+j+1])
      #                  print num
                        if num < 256:
                            #string = string + (str(num)+'.')
                            self.solve(s,i+1,begin+j+1,res,string + (str(num)+'.'))
                            #string = string[0:begin]

A = Solution()
print A.restoreIpAddresses("25525511135")
print A.restoreIpAddresses("010010")