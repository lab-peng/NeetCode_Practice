from typing import List
from collections import Counter


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

    def characterReplacement(self, s: str, k: int) -> int:
        """
        424. Longest Repeating Character Replacement
        :param s:
        :param k:
        :return:
        """
        count, l, most_common, longest = {}, 0, 0, 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            most_common = max(most_common, count[s[r]])
            while (r - l + 1) - most_common > k:  # r - l + 1 == window_size
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest

    def minWindow(self, s: str, t: str) -> str:
        """
        76. Minimum Window Substring
        :param s:
        :param t:
        :return:
        """
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        l, hm = 0, {}
        have, need = 0, len(count_t)
        res, min_window = [-1, -1], float("inf")

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            # print(hm, count_t)
            if s[r] in count_t and hm[s[r]] == count_t[s[r]]:
                have += 1

            while have == need and l <= r:
                if (r - l + 1) < min_window:
                    res = [l, r]
                    min_window = r - l + 1
                hm[s[l]] -= 1
                if s[l] in count_t and hm[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        # return s[l: r+1] if min_window != float('inf') else ''  # No need s[-1:0] == ''
        return s[l: r + 1]


solution = Solution()

prices = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices))

s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))

s, k = "ABAB", 2
s, k = "AABABBA", 1
# s, k = 'ABABBA', 2
print(solution.characterReplacement(s, k))


s, t = "ADOBECODEBANC", "ABC"
# s, t = 'a', 'a'
# s, t = 'a', 'aa'
print(solution.minWindow(s, t))
