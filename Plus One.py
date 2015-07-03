class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if not digits:
            return None
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if i == 0 and digits[0] == 0:
            digits.insert(0,1)
        return digits

A = Solution()
print  A.plusOne([1,2,3,4,5])
print  A.plusOne([1,2,3,4,9])
print  A.plusOne([9])
print  A.plusOne([9,9,9,9,9])
print  A.plusOne([1])