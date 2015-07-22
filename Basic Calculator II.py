class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        flag = []
        nums = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                for j in xrange(i,len(s)):
                    if not s[j].isdigit():
                        break
                if j == len(s) - 1 and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                nums.append(num)
                i = j - 1
            if s[i] in ['+','-','*','/']:
                flag.append(s[i])
            i += 1

        if not nums:
            return 0
        res = nums[0]
        i = 0
        #print nums,flag
        while i < len(flag):
            if flag[i] == '*':
                res *= nums[i+1]
            elif flag[i] == '/':
                res = int(res / float(nums[i+1]))
            else:
                if i + 1 < len(flag) and flag[i+1] in ['*','/']:
                    temp = nums[i+1]
                    for j in xrange(i+1,len(flag)):
                        if flag[j] == '*':
                            temp = temp * nums[j+1]
                        elif flag[j] == '/':
                            temp = int(float(temp) / nums[j+1])
                        else:
                            break
                    if flag[i] == '+':
                            res += temp
                    else:
                            res -= temp
                    if flag[j] in ['*','/']:
                        i = j
                    else:
                        i = j - 1
                else:
                    if flag[i] == '+':
                        res += nums[i+1]
                    else:
                        res -= nums[i+1]
            i += 1
            #print res
        return res

A = Solution()
print A.calculate("2*3 + 3*4 -2*2/3*5+4")
print A.calculate("100000000/1/2/3/4/5/6/7/8/9/10")
print A.calculate("3-66/10")
print A.calculate("1/1/2/3/4/5/6/7/8/9/10")