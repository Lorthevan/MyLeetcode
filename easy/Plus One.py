class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def binary(i):
            digits[i] = digits[i]+1
            if digits[i] >= 10:
                digits[i] = digits[i] - 10
                if i == 0:
                    digits.insert(0,0)
                    i += 1
                binary(i-1)
        binary(len(digits)-1)
        return digits