class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        
        def traceback(candidates, target, cell):
            if target == 0:
                res.append(cell)
            for i, num in enumerate(candidates):
                if target >= num:
                    traceback(candidates[i:], target - num, cell + [num])
                else:
                    break
        
        traceback(candidates, target, [])
        return res