class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        begin = 1
        if not n:
            return ""
        strint = str(begin)
        for i in range(n-1):
            temp = ""
            size = len(strint)
            j = 0
            while j < size:
                a = strint[j]
                base = j
                j += 1
                while j < size and strint[j] == a:
                    j += 1
                temp += (str(j - base) + a)
            strint = temp
        return strint

A = Solution()
print A.countAndSay(1)
print A.countAndSay(2)
print A.countAndSay(3)
print A.countAndSay(4)
print A.countAndSay(5)
print A.countAndSay(6)
print A.countAndSay(7)
print A.countAndSay(8)