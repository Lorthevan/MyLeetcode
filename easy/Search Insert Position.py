class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binary_search(target, left, right):
            if right >= left:
                middle = (left + right) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    return middle
                return binary_search(target, left, right)
            else:
                return left
        
        return binary_search(target, 0, len(nums) - 1)