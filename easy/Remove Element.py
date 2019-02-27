class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while 1:
            if val in nums:
                nums.remove(val)
            else:
                break
        return len(nums)