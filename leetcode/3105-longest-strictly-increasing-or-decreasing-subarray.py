# Problem: 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# Link: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
# Difficulty: Easy
# Approach: Single pass tracking current increasing and decreasing run lengths
# Time: O(n), Space: O(1)

class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        inc = dec = best = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1

            best = max(best, inc, dec)

        return best