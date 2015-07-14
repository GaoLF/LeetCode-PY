#coding=utf-8
class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    # 感觉应该用分治法来做，但我也就图省事了，利用加法做的
    # 然后把一个数的从乘以0 到乘以9加入一个map中，可以节省一些时间
    def multiply(self, num1, num2):
        res = ""
        len1 = len(num1)
        len2 = len(num2)
        dic = {}
        if len1 < len2:
            num1,num2,len1,len2 = num2,num1,len2,len1
        temp = ""
        for i in xrange(10):
            dic[i] = temp
            temp = self.add(num1,temp)
        for i in xrange(len2):
            num = int(num2[i:i+1])
            temp = dic[num]
            if res:
                res = res + "0"
            res = self.add(res,temp)
        return res

    def add(self,nums1,nums2):
        if not nums1 and not nums2:
            return "0"
        carry = 0
        size1,size2 = len(nums1)-1,len(nums2)-1

        res = ""
        while size1 >= 0 or size2 >= 0:
            if size1 >= 0:
                a = int(nums1[size1:size1+1])
            else:
                a = 0
            if size2 >= 0:
                b = int(nums2[size2:size2+1])
            else:
                b = 0
            sum_v = (a + b + carry)%10
            carry = (a + b + carry)/10
            res = str(sum_v) + res
            size1 -= 1
            size2 -= 1
        if carry:
            res = '1' + res
        return res

A = Solution()
print A.multiply("0","0")
print A.multiply("8364706555694632506241942061841807278055516979340976383589685785705700271160027216944215305094666159386415617", "4815589832802040613226282551626238706601093398571913553809993718598371680031000194671")