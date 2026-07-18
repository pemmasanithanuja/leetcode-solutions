class Solution:
    def countHousePlacements(self, n):
        MOD = 10**9 + 7

        # ways[i] = number of ways to place houses on one side of street
        a = 1  # no house at current position
        b = 2  # house or no house at current position

        for _ in range(2, n + 1):
            a, b = b, (a + b) % MOD

        # Both sides of street are independent
        return (b * b) % MOD