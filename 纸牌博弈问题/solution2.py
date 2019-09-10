class Solution_1d:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True
        dp = [[0] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][-1] >= 0


class Solution_1d:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True
        dp = [0] * n
        for i in reversed(range(n)):
            dp[i] = nums[i]
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0

