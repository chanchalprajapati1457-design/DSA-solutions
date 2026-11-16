# Problem: 2243. Calculate Digit Sum of a String
# Link: https://leetcode.com/problems/calculate-digit-sum-of-a-string/
# Difficulty: Easy
# Approach: Simulate rounds. Split into groups of k, replace each group by its digit sum.
# Time: O(n log n) in practice (string shrinks every round), Space: O(n)

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            parts = []
            for i in range(0, len(s), k):
                group = s[i:i + k]
                parts.append(str(sum(int(ch) for ch in group)))
            s = "".join(parts)
        return s