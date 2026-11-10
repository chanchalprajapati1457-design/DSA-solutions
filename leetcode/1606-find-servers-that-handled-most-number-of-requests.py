# Problem: 1606. Find Servers That Handled Most Number of Requests
# Link: https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
# Difficulty: Hard
# Approach: SortedList for free servers + min-heap for busy servers
# Time: O(n log k), Space: O(k)
import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k, arrival, load):
        available = SortedList(range(k))
        busy = []
        
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            # Free servers whose requests are completed
            while busy and busy[0][0] <= time:
                end_time, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            # Find next available server
            target = i % k
            idx = available.bisect_left(target)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            count[server] += 1

            # Mark server as busy
            heapq.heappush(
                busy,
                (time + load[i], server)
            )

        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]
        