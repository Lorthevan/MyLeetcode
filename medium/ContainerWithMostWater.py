class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # m = 0
        # for x, y in enumerate(height):
        #     for a, b in enumerate(height[x+1:]):
        #         m = max((a+1) * min(y, b), m)
        # return m
        
        m, left, right = 0, 0, len(height) - 1
        while left != right:
            m = max((right - left) * min(height[left], height[right]), m)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return m