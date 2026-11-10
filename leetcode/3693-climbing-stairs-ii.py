# Problem: 3693. Climbing Stairs II
# Link: https://leetcode.com/problems/climbing-stairs-ii/
# Difficulty: Medium
# Approach: DP, dp[j] = min(dp[j-k] + costs[j] + k*k) for k in 1..3
# Time: O(n), Space: O(n)

class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        for j in range(1, n + 1):
            for k in range(1, 4):
                if j - k >= 0:
                    dp[j] = min(dp[j], dp[j - k] + costs[j - 1] + k * k)

        return dp[n]