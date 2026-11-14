# Problem: 3505. Minimum Operations to Make Elements Within K Subarrays Equal
# Link: https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/
# Difficulty: Hard
# Approach: Sliding window median using Fenwick Tree + DP

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit_mask >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        count = Fenwick(m)
        sums = Fenwick(m)

        costs = []
        window_sum = 0

        for i in range(n):
            v = nums[i]
            r = rank[v]

            count.update(r, 1)
            sums.update(r, v)
            window_sum += v

            if i >= x:
                old = nums[i - x]
                r_old = rank[old]

                count.update(r_old, -1)
                sums.update(r_old, -old)
                window_sum -= old

            if i >= x - 1:
                # Find median
                mid_rank = count.kth((x + 1) // 2)
                median = vals[mid_rank - 1]

                # Calculate sum of left side
                left_count = count.query(mid_rank)
                left_sum = sums.query(mid_rank)

                right_count = x - left_count
                right_sum = window_sum - left_sum

                cost = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )

                costs.append(cost)

        # Dynamic Programming
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element
                curr[i] = curr[i - 1]

                # Take subarray ending at i-1
                if i >= x:
                    start = i - x

                    candidate = prev[start] + costs[start]

                    curr[i] = min(curr[i], candidate)

            prev = curr

        return prev[n]