class Solution:
    def climbstairs(self, n):
        """
        :type n: int
        :rtype: int
        Fibonacci sequence: 1 2 3 5 8 ...
        """
        if n == 1:      #border
            return 1
        elif n == 2:    #border
            return 2
        else:
            a, b = 1, 2
            for i in range(2, n):
                a, b = b, a+b   #state-transition equation
            return b


x = Solution()
print(x.climbstairs(6))