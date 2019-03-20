class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if nums[i] == 0 and i != 0:
                nums.insert(0, nums.pop(i))
                if len(set(nums[0:i+1])) == 1:
                    i += 1
            elif nums[i] == 2 and i != len(nums) - 1:
                nums.append(nums.pop(i))
                if len(set(nums[i:])) == 1:
                    break
            else:
                i += 1