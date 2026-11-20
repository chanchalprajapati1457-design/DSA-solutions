# Problem: 3041. Maximize Consecutive Elements in an Array After Modification
# Link: https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/
# Difficulty: Hard
# Approach: Sort, then dp[v] = longest consecutive chain ending at value v.
#           Each x can stay x or become x + 1.
#           Update dp[x + 1] before dp[x] so one element is not used twice.
# Time: O(n log n), Space: O(n)

class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp = {}

        for x in nums:
            dp[x + 1] = dp.get(x, 0) + 1
            dp[x] = dp.get(x - 1, 0) + 1

        return max(dp.values())