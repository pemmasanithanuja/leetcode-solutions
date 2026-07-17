class Solution:
    def minimumTotal(self, triangle):
        # Copy the last row
        dp = triangle[-1][:]

        # Start from the second last row
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]