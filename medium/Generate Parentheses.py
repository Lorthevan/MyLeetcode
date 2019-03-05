class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()
        
        def backtrace(cell='', left=0, right=0):
            if len(cell) == 2 * n:
                res.append(cell)
                return
            if left < n:
                backtrace(cell + '(', left + 1, right)
            if left > right:
                backtrace(cell + ')', left, right + 1)
        
        backtrace()
        return res