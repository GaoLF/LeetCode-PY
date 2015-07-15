#coding=utf-8
class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
    # 答案的方法又是比我的要好太多，我之前C++写的就是正向走，遇到负值，前边的都部分+1
    # 答案的方法是走两遍，然后正向一遍负向一遍
    # 正向的能大体确认后一个值比前一个值大的情况，但也有例外，例外需要反向进行操作
        vec = [1 for i in xrange(len(ratings))]
        for i in xrange(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                vec[i] = vec[i-1] + 1
        for i in xrange(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i + 1]:
                vec[i] = max(vec[i],vec[i+1] + 1)
        res = 0
        for num in vec:
            res += num
        #print vec
        return res

A = Solution()
print A.candy([1,2,3,2,5,2,4,3,2,1])
print A.candy([1])
print A.candy([])
