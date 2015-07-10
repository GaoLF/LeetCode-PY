class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        len = -1
        if x <= 0:
            return 0
        temp = x
        while temp:
            temp >>= 1
            len += 1
        begin = 1 << (len / 2)
        end = begin << 1
        #print "(",begin,end,")",
        step = 1
        flag = 0
        while begin <= end:
            if begin**2 < x:
                #print begin**2,x,"!"
                if (begin+2*step)**2 < x:
                    step += step
                    begin += step
                else:
                    step = 1
                    begin += 1
            elif begin**2 > x:
                return begin - 1
            else:
                return begin

     #   if begin*begin <= x:
       #     return begin
      #  else:
      #      return begin - 1


A = Solution()
for i in range(100):
    print i,A.mySqrt(i)