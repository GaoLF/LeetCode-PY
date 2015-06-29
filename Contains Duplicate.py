class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    #---------------------------------PythonÖĞÒ²ÓĞset£¡£¡£¡
    def containsDuplicate(self, nums):
        set_l = set(nums)
        if len(set_l) == len(nums):
            return False
        else:
            return True
    """ -------------------------------Time Limit Exceeded
    def containsDuplicate(self, nums):
        for num in nums:
            if nums.count(num)>1:
                return False
        return True
    """
    """ -------------------------------Time Limit Exceeded
    def containsDuplicate(self, nums):
        set = []
        for num in nums:
            if num not in set:
                set.append(num)
            else:
                return False
        return True
    """