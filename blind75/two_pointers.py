from typing import List
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # processed_str = ''
        # for c in s:
        #     if c.isalnum():
        #         processed_str += c.lower()
        processed_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l, r = 0, len(processed_str) - 1
        while l <= r:
            if processed_str[l] != processed_str[r]:
                return False
            l += 1
            r -= 1
        return True

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = v + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    ans.append([v, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))

nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(solution.maxArea(height))
