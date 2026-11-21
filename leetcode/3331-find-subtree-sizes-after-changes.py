# Problem: 3331. Find Subtree Sizes After Changes
# Link: https://leetcode.com/problems/find-subtree-sizes-after-changes/
# Difficulty: Medium
# Approach: Iterative DFS keeping last[c] = closest ancestor with letter c to find
#           each node's new parent. Then accumulate sizes in reverse preorder
#           (a new parent always appears before its child in preorder).
# Time: O(n), Space: O(n)

class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26      # closest ancestor (original tree) for each letter
        saved = [-1] * n      # value of last[c] before entering this node
        order = []            # preorder of the original tree
        stack = [(0, False)]

        while stack:
            node, done = stack.pop()
            c = ord(s[node]) - 97
            if done:
                last[c] = saved[node]   # backtrack
                continue

            order.append(node)
            if node != 0 and last[c] != -1:
                new_parent[node] = last[c]
            saved[node] = last[c]
            last[c] = node

            stack.append((node, True))
            for ch in children[node]:
                stack.append((ch, False))

        size = [1] * n
        for node in reversed(order):
            if node != 0:
                size[new_parent[node]] += size[node]

        return size