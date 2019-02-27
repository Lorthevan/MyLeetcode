class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # map = {
        #     'M': 1000,
        #     'D': 500,
        #     'C': 100,
        #     'L': 50,
        #     'X': 10,
        #     'V': 5,
        #     'I': 1,
        # }
        # s = ''
        # for c, i in map.items():
        #     count, num = divmod(num, i)
        #     s += c*count
        #     s = s.replace('VIIII', 'IX').replace('LXXXX', 'XC').replace('DCCCC', 'CM').replace('IIII','IV').replace('XXXX', 'XL').replace('CCCC', 'CD')
        # return s
        
        M = ("", "M", "MM", "MMM")
        C = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
        X = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
        I = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]