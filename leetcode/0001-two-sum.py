# Problem: 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Approach: HashMap, Time O(n), Space O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i