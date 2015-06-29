class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n == 0:
            return 0
        res_l = [1]
        i = 1
        while i <= n:
            sum = 0
            j = 0
            while j < i:
                sum += res_l[j]*res_l[i-j-1]
                j += 1
            i += 1
            res_l.append(sum)
        return res_l[n]