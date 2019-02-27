class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        res = list()
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mon',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        def backtrack(cell, numbers):
            if not numbers:
                res.append(cell)
                return

            letters = dic[numbers[0]]
            for i in range(len(letters)):
                backtrack(cell+letters[i], numbers[1:])
        if digits:
            backtrack('', digits)
        return res