# Problem: 3420. Count Non-Decreasing Subarrays After K Operations
# Link: https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
# Difficulty: Hard
# Approach: cost(l, r) = sum(prefix_max - nums[i]) is monotone in l, so use two pointers.
#           Sum of prefix maxima is computed in O(1) using next-greater chain sums (S)
#           and a monotonic deque that gives the first max position in the window.
# Time: O(n), Space: O(n)

from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Prefix sums of nums
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]

        # Next strictly greater element and chain sums S
        S = [0] * (n + 1)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            ng = stack[-1] if stack else n
            S[i] = nums[i] * (ng - i) + S[ng]
            stack.append(i)

        dq = deque()
        l = 0
        ans = 0

        for r in range(n):
            # Keep equal values so the front is the FIRST max position
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            while True:
                while dq[0] < l:
                    dq.popleft()
                c = dq[0]
                pref_max_sum = S[l] - S[c] + nums[c] * (r - c + 1)
                cost = pref_max_sum - (P[r + 1] - P[l])
                if cost <= k:
                    break
                l += 1

            ans += r - l + 1

        return ans