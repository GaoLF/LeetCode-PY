#coding=utf-8
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    # *********************************************************************************
    # **********************************用最老土的方法*********************************
    # **********************************巧妙地用不了的！*******************************
    # **注意一点，要比较两种情况s1中(0,i)(i,size)两块与s2的(0,i)(i,size)两块进行比较***
    #*******************以及s1的(0,i)(i,size)两块与s2的(size-i)(0,i)进行比较***********
    # *********************************************************************************
    # *********************************************************************************
    def isScramble(self, s1, s2):
        #print s1,s2
        len1 = len(s1)
        len2 = len(s2)
        if len1 != len2:
            return False
        if s1 == s2:
            return True
        a = [i for i in s1]
        b = [i for i in s2]
        a.sort()
        b.sort()
        if a != b:
            return False
        for i in range(1,len1):
            if self.isScramble(s1[0:i],s2[0:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[0:i],s2[len1-i:]) and self.isScramble(s1[i:],s2[:len1-i]):
                return True
        return False

A = Solution()
print A.isScramble('rgtae',"great")