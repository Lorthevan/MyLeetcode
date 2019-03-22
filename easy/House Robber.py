class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length in [1, 2]:
            return max(nums)
        val_max = [-1] * length
        val_max[0] = nums[0]
        val_max[1] = max(nums[0], nums[1])
        i = 2
        while i < length:
            val_max[i] = max(val_max[i - 1], val_max[i - 2] + nums[i])
            i += 1
        return val_max[length - 1]

#         if len(nums) == 0:
#             return 0
#         def max_rob(i):
#             if i == 0:
#                 return nums[i]
#             if i == 1:
#                 return max(nums[0], nums[1])
#             return max(max_rob(i-1), max_rob(i-2) + nums[i])

#         return max_rob(len(nums)-1)
