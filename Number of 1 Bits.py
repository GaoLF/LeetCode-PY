class Solution:
    # @param n, an integer
    # @return an integer
    #python太可怕了，好像都不用考虑无符号数的问题！
    def hammingWeight(self, n):
        foo = 1
        res = 0
        for i in range(1,33):
            bar = foo & n
            if bar != 0:
                res = res + 1
            foo = 1 << i
        return res