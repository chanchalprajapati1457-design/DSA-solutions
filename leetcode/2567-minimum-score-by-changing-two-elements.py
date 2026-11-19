# Problem: 2567. Minimum Score by Changing Two Elements
# Link: https://leetcode.com/problems/minimum-score-by-changing-two-elements/
# Difficulty: Medium
# Approach: Low score can always be made 0 with two changes, so minimize
#           the high score by sorting and checking 3 cases.
# Time: O(n log n), Space: O(1) extra

class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        return min(
            nums[-1] - nums[2],   # remove the two smallest
            nums[-2] - nums[1],   # remove the smallest and the largest
            nums[-3] - nums[0],   # remove the two largest
        )