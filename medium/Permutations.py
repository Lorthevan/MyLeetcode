class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def traceback(nums, cell):
            if not nums:
                res.append(cell)
            for i, num in enumerate(nums):
                subnums = nums.copy()
                subnums.pop(i)
                traceback(subnums, cell + [num])
        
        res = []
        traceback(nums, [])
        return res