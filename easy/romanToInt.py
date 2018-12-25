class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic ={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        rtype = 0
        for i in range(0,len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                rtype -= dic[s[i]]
            else:
                rtype += dic[s[i]]
        rtype += dic[s[-1]]
        return rtype