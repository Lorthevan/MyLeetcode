class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        i, j = 0, len(s)
        s = "#" + s + "#"
        
        while j > 0:
            for i in range(1, len(s) - j):
                if s[i:i + j] == s[i + j - 1:i - 1:-1]:
                    return s[i:i + j]
            j -= 1
