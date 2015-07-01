class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, s):
        count = 0
        res = ""
        ones = ['M','C','X','I']
        fives = ['','D','L','V']
        while s!=0:
            flag = int(s)/1000
            if flag < 4:
                res += flag*ones[count]
            elif flag == 4:
                res += ones[count]+fives[count]
            elif flag == 9:
                res += ones[count]+ones[count-1]
            else:
                res += fives[count]+(flag-5)*ones[count]
            s = (s%1000)*10
            count += 1
        return res

A = Solution()
print A.intToRoman(1899)
print A.intToRoman(599)
print A.intToRoman(9)
print A.intToRoman(4)
print A.intToRoman(1888)