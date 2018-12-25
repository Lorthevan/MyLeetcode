class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if x < 0:
            sym = '-'
            s = s[1:]

            s = s[::-1]
        elif x > 0:
            sym = ''
            s = s[::-1]
        else:
            return 0
        res = int(sym+s.lstrip('0'))
        if res >= -2**31 and res <= 2**31-1:
            return res
        else:
            return 0