class Solution(object):
    def maxProfit(self, prices):
        left, right = 0, 1
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                maxP += prices[right] - prices[left]
            left = right
            right += 1
        return maxP