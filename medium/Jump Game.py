class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if not nums:
            return True
        last = nums[0]
        for position, step in enumerate(nums):
            if position <= last and last <= position + step:
                last = position + step
        return last >= len(nums) - 1