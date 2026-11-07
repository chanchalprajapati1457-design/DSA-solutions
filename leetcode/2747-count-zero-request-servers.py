# Problem: 2747. Count Zero Request Servers
# Link: https://leetcode.com/problems/count-zero-request-servers/
# Difficulty: Medium
# Approach: Sort logs and queries, sliding window with a count dictionary
# Time: O(L log L + Q log Q), Space: O(n)

class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        cnt = {}
        ans = [0] * len(queries)
        left = right = 0
        m = len(logs)

        for qi in order:
            q = queries[qi]

            # Add logs with time <= q
            while right < m and logs[right][1] <= q:
                s = logs[right][0]
                cnt[s] = cnt.get(s, 0) + 1
                right += 1

            # Remove logs with time < q - x
            while left < right and logs[left][1] < q - x:
                s = logs[left][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    del cnt[s]
                left += 1

            ans[qi] = n - len(cnt)

        return ans