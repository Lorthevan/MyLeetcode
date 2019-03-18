class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if nums[i] not in nums[i+1:] and nums[i] not in nums[0:i]:
        #         return nums[i]
        return 2*sum(set(nums))-sum(nums)