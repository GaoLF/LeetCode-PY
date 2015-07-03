#coding=utf-8
class Solution:
    # @param nums, an integer[]
    # @return an integer
    # 这个题很巧妙，之前我在想如果一个数组是1,2,3,5,4,5,6
    # 难以确定峰值的位置！但是这个题目要求-1和n位置都是负无穷，因此这个list还有一个
    # 峰值，就是6！所以这个题目完全可以通过二叉树进行查找
    # 找区间中间的两个连续数，相比较，如果a<b，意味着是左边是上升的，不一定有峰值，右边是先上后下降的，一定有
    # 反之，a>b,左边一定是先上后下的
    def findPeakElement(self, nums):
        begin = 0
        end = len(nums)-1
        while begin < end:
            mid = (begin + end)/2
            if nums[mid] < nums[mid+1]:
                begin = mid + 1
            else:
                end = mid
        return begin

    """ 如果顺序搜索更简单，只要找到第一个元素比他的前一个小的即可
        int findPeakElement(const vector<int> &num) {
        for(int i = 1; i < num.size(); i ++)
        {
            if(num[i] < num[i-1])
            {// <
                return i-1;
            }
        }
        return num.size()-1;
    }
    """

A = Solution()
print A.findPeakElement([])
print A.findPeakElement([1,2])
print A.findPeakElement([1,2,3,4,5])
print A.findPeakElement([1,2,3,4,6,5,6,7])