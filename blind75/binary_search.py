from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        153. Find Minimum in Rotated Sorted Array
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
        """
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]


nums = [3, 4, 5, 1, 2]
s = Solution()
print(s.findMin(nums))


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        33. Search in Rotated Sorted Array
        https://leetcode.com/problems/search-in-rotated-sorted-array/
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
s = Solution()
print(s.search(nums, target))
