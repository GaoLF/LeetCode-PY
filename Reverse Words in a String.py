#coding=utf-8
#---------------------------------------------------------#
#** 方法很简单，记得之前一个题做过，把所有的单词都压入一个vec中  **#
#** 然后把所有的单词再加起来，一个值得注意的地方就是加单词的时候  **#
#** 我都是以当前是空格然后把之前的单词组合压入vec，但是如果到了  **#
#** 字符串的最后一个，别忘了也加进去，如果不是" "则把他加进去 !  **#
#---------------------------------------------------------#
class Solution:
    # @param s, a string
    # @return a string

    def reverseWords(self, s):
        size = len(s)
        if not s:
            return s
        begin = i = 0
        vec = []

        while i < size:
            if s[i:i+1] == ' ':
                if i != begin:
                    vec.append(s[begin:i])
                begin = i + 1
            i += 1
        if s[size-1]!=' ':
            vec.append(s[begin:])
        res = ""
        for iter in vec[::-1]:
            res += " "+ iter
        return res[1:]


A = Solution()
print A.reverseWords("a  the sky   is blue")+"!"
print A.reverseWords("  a  the sky   is blue   ")+"!"
print A.reverseWords("a")+"!"

