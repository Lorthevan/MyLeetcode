class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # for i,v in enumerate(nums):
        #     if target == v:
        #         return i
        # else:
        #     return -1
        
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if target < nums[0] < nums[mid]:
                left = mid + 1
            elif target > nums[0] > nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            else:
                return left
        else:
            return -1