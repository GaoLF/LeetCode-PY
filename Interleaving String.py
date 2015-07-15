#coding=utf-8
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    # 我这个方法可能是比较麻烦的，也没有用动态规划
    # 我的方法是挨个检测s3 与 s1 和s2 的该位置是否相同
    # 与其中一个相同，往下走，都不相同返回False，这都很简单
    # 如果与s1 和 s2 都相同，找到s1，s2,s3中该字母重复出现的个数
    # 然后把s3移到下一个不等于当前字母的位置，s1和s2只保证一个移到下一个不等于当前字母的位置
    # 递归下去
    # 别人的方法是我注释起来的这一段，很短用的动态规划
    # 别人的方法是这样的，如果当前满足条件，把满足条件的都压入栈中，但是如果相同的字母很多的话，我觉得栈的长度会很长吧
    # 如果1个满足就压一个，如果两个满足就都压入，下一次循环的时候把上一次满足条件的都检测一遍
    #　感觉这也是一个很好的思路啊，我猜不如我的速度快
    """
    def isInterleave(self, s1, s2, s3):
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False

        last = set([(0, 0)])
        for char in s3:
            current = set()
            for i, j in last:
                if i < l1 and s1[i] == char:
                    current.add((i + 1, j))
                if j < l2 and s2[j] == char:
                    current.add((i, j + 1))
            if not current:
                return False
            last = current
        return True
    """
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        return self.check(s1,s2,s3,0,0,0)
    def check(self,s1,s2,s3,i1,i2,i3):
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if i1 == len1:
            if s2[i2:] == s3[i3:]:
                return True
            else:
                return False
        if i2 == len2:
            if s1[i1:] == s3[i3:]:
                return True
            else:
                return False
        if i3 == len3:
            return False
        c1, c2, c3 = s1[i1:i1+1], s2[i2:i2+1], s3[i3:i3+1]
        if c3 == c2 and c3 == c1:
            sames1 = sames2 = sames3 = 1
            temp1, temp2, temp3 = i1 + 1,i2 + 1,i3 + 1
            while temp1 < len1 and s1[temp1:temp1+1] == c1:
                sames1 += 1
                temp1 += 1
            while temp2 < len2 and s2[temp2:temp2+1] == c2:
                sames2 += 1
                temp2 += 1
            while temp3 < len3 and s3[temp3:temp3+1] == c3:
                sames3 += 1
                temp3 += 1
            if sames3 > sames1 + sames2 or (sames3 < sames1 and sames3 < sames2):
                return False
            if self.check(s1,s2,s3,i1+sames1,i2+sames3-sames1,i3+sames3):
                return True
            else:
                return self.check(s1,s2,s3,i1+sames3-sames2,i2+sames2,i3+sames3)
        elif c3 == c1:
            return self.check(s1,s2,s3,i1+1,i2,i3+1)
        elif c3 == c2:
            return self.check(s1,s2,s3,i1,i2+1,i3+1)
        else:
            return False

A = Solution()
print A.isInterleave("aa","ab","aaba")
print A.isInterleave("aa","ab","abaa")
print A.isInterleave("aabcc","dbbca","aadbbcbcac")
print A.isInterleave("aabcc","dbbca","aadbbbaccc")