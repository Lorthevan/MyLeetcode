class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxfit = 0
        if prices == []: return 0
        minnum = max(prices)
        for i in range(len(prices)):
            if prices[i] < minnum:
                minnum = prices[i]
            elif maxfit < prices[i] - minnum:
                maxfit = prices[i] - minnum
        return maxfit