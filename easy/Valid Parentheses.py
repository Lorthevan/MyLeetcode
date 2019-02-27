class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        mapping = {")": "(", "}": "{", "]": "["}
        s = s.replace(' ','')
        if s == '':
            return False
        for i in range(len(s)//2+1):
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
        return False if s != '' else True