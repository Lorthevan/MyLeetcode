class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first, last = 0, 0
        i, j = 0, 0
        
        for i in range(len(nums)):
            if nums[i] == target:
                first = i
                break
        else:
            return [-1, -1]
        
        for j in range(i + 1, len(nums)):
            if nums[j] != target:
                last = nums[j - 1]
                return [i, j - 1]
        else:
            return [i, j or i]