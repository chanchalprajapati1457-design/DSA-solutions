# Problem: 2911. Minimum Changes to Make K Semi-palindromes
# Link: https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/
# Difficulty: Hard
# Approach: Precompute cost[i][j] (min changes to make s[i..j] a semi-palindrome
#           over all divisors d of its length), then DP over k partitions.
# Time: O(n^3 + k * n^2), Space: O(n^2)

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = INF
                for d in range(1, length):
                    if length % d != 0:
                        continue
                    m = length // d
                    changes = 0
                    for r in range(d):
                        for t in range(m // 2):
                            if s[i + r + t * d] != s[i + r + (m - 1 - t) * d]:
                                changes += 1
                    best = min(best, changes)
                cost[i][j] = best

        # dp[p][j] = min changes to split first j characters into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] < INF:
                        dp[p][j] = min(dp[p][j], dp[p - 1][i] + cost[i][j - 1])

        return dp[k][n]