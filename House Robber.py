#coding=utf-8
# 刚做的时候我还在想这个问题肯定不能用动态规划了
# 实际上一个节点作为动态规划确实不能做，但是表示两个点的动态规划确实是可以做的！！！！
class Solution:
    # @param {integer[]} nums
    # @return {integer}

    """
    貌似我写的这个方法还是不够好，是参照一个别人写的
    下边这种C++写的好像更好
    int pre2 = 0, cur2 = 0;
    for(int i = 1; i < nums.size(); ++ i)
    {
        int temp = pre2;
        pre2 = cur2;
        cur2 = max(temp + nums[i], pre2);
    }

    return max(cur1, cur2)
    """
    def rob(self, nums):
        start_with_zero = 0
        start_with_one  = 0
        for i in range(len(nums)):
            if not i%2: # start with 0
                start_with_zero = max(start_with_zero + nums[i],start_with_one)
            else:
                start_with_one = max(start_with_one + nums[i],start_with_zero)
        return max(start_with_one,start_with_zero)

#***********************************************************************************
#****************************这个方法肯定不是最优***********************************
#********************************需要继续考究***************************************
#***********************************************************************************
#这个方法就是用递归的方法，然后遇到的每个点的max值都存在一个字典里，其实复杂度也不高，但是方法看起来笨笨的

    """
    def rob(self, nums):
        x = {}
        return self.check(nums,x)

    def check(self,nums,x):
        size = len(nums)
        if size in x:
            return x[size]
        if not size:
            return 0
        if size == 1:
            return nums[0]
        left = self.check(nums[2:],x)
        right = self.check(nums[1:],x)
        x[size - 2] = left
        x[size - 1] = right
        return max(left + nums[0],right)
        """

A = Solution()
print A.rob([1,2,3,4,5,6,7])
print A.rob([1,2])
print A.rob([1,2,3,4,5,6,7,8])
print A.rob([])
print A.rob([1])