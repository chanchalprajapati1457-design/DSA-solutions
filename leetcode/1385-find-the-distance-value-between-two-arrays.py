# Problem: 1385. Find the Distance Value Between Two Arrays
# Link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Difficulty: Easy
# Approach: Brute force with early break, Time O(n*m), Space O(1)
from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0

        for a in arr1:
            i = bisect_left(arr2, a)
            ok = True
            if i < len(arr2) and arr2[i] - a <= d:
                ok = False
            if i > 0 and a - arr2[i - 1] <= d:
                ok = False
            if ok:
                count += 1

        return count