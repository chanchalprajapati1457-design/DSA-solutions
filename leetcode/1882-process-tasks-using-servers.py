# Problem: 1882. Process Tasks Using Servers
# Link: https://leetcode.com/problems/process-tasks-using-servers/
# Difficulty: Medium
# Approach: Two heaps (free servers by weight/index, busy servers by free time)
# Time: O((n + m) log n), Space: O(n)

import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []
        time = 0

        for j, t in enumerate(tasks):
            time = max(time, j)

            # No free server: jump to the earliest time one becomes free
            if not free and busy[0][0] > time:
                time = busy[0][0]

            # Release all servers that are done by now
            while busy and busy[0][0] <= time:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (time + t, w, i))

        return ans