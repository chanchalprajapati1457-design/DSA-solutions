# Problem: 3789. Minimum Cost to Acquire Required Items
# Link: https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
# Difficulty: Medium
# Approach: Cost as a function of type-3 items x is convex and piecewise linear,
#           so only check x = 0, min(need1, need2), max(need1, need2).
# Time: O(1), Space: O(1)

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def total(x: int) -> int:
            return (x * costBoth
                    + max(0, need1 - x) * cost1
                    + max(0, need2 - x) * cost2)

        lo, hi = min(need1, need2), max(need1, need2)
        return min(total(0), total(lo), total(hi))