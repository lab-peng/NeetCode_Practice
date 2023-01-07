from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        3. Longest Substring Without Repeating Characters
        :param s:
        :return:
        """
        hs = set()
        l, r, longest = 0, 0, 0

        while r < len(s):
            while s[r] in hs:
                # Note: we should remove s[l] before incrementing l or we would have removed the wrong element
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            longest = max(longest, len(hs))
            r += 1
        return longest


solution = Solution()

prices = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices))

s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))