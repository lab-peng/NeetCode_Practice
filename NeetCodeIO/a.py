from typing import List
from collections import defaultdict
from itertools import combinations, accumulate


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        149. Max Points on a Line
        https://leetcode.com/problems/max-points-on-a-line/
        """
        max_p = 0
        for i in range(len(points)):
            p1 = points[i]
            count = defaultdict(int)
            for j in range(i + 1, len(points)):
                p2 = points[j]
                slope = (p1[1] - p2[1]) / (p1[0] - p2[0]) if p1[0] != p2[0] else float('inf')
                count[slope] += 1
            max_count = max(count.values()) if count.values() else 0
            max_p = max(max_p, max_count + 1)
        return max_p


points = [[1, 1], [2, 2], [3, 3]]
points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
s = Solution()
print(s.maxPoints(points))

print(list(accumulate([0, 1, 2, 3])))
