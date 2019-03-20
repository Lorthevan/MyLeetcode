class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        res = [0]
        
        def traceback(x, y, res=res):
            if x >= m or y >= n:
                return
            if x == m - 1 and y == n - 1:
                res[0] += 1
                return
            traceback(x + 1, y)
            traceback(x, y + 1)
        
        traceback(0, 0)
        return res[0]