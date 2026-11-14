# Problem: 3364. Minimum Positive Sum Subarray
# Link: https://leetcode.com/problems/minimum-positive-sum-subarray/
# Difficulty: Easy
# Approach: Brute force over all subarrays with size in [l, r] using prefix sums
# Time: O(n * (r - l + 1)), Space: O(n)

class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        best = float('inf')

        for size in range(l, r + 1):
            for i in range(n - size + 1):
                total = prefix[i + size] - prefix[i]
                if total > 0:
                    best = min(best, total)

        return best if best != float('inf') else -1