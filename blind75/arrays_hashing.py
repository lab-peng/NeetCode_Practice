from typing import List
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = countS.get(s[i], 0) + 1
        #     countT[t[i]] = countT.get(t[i], 0) + 1
        # return countS == countT

        countS = [0] * 26
        for c in s:
            countS[ord(c) - ord('a')] += 1
        countT = [0] * 26
        for c in t:
            countT[ord(c) - ord('a')] += 1
        return countS == countT

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in hm:
                return [hm[complement], i]
            hm[v] = i
        return -1

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            hm[key].append(s)
            # print(hm)
        return hm.values()

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        sorted_keys = sorted(count, key=count.get, reverse=True)
        return sorted_keys[:k]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

    def encode(self, strs):
        return ':#;'.join(strs)

    def decode(self, str):
        return str.split(':#;')

    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in hs:
                length = 1
                while (n + length) in hs:
                    length += 1
                longest = max(length, longest)
        return longest


solution = Solution()
nums = [1, 2, 3, 4, 4]
print(solution.containsDuplicate(nums))

s = 'anagram'
t = 'nagaram'
print(solution.isAnagram(s, t))

nums, target = [2, 7, 11, 15], 22
print(solution.twoSum(nums, target))

strs = ["nat", "tea", "tan", "ate", "eat", "bat"]
print(solution.groupAnagrams(strs))

nums, k = [1, 1, 1, 2, 2, 3], 2
print(solution.topKFrequent(nums, k))

nums = [1, 2, 3, 4]
print(solution.productExceptSelf(nums))

strs = ["lint", "code", "love", "you"]
print(solution.encode(strs))
print(solution.decode(solution.encode(strs)))

nums = [100, 4, 200, 1, 3, 2]
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print(solution.longestConsecutive(nums))
