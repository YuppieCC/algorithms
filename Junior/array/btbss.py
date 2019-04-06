class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                max_profit += profit
        return max_profit


if __name__ == '__main__':
    ip = [3, 3, 6, 7, 0, 0, 1, 4]
    op = Solution().maxProfit(ip)
    print(op)
