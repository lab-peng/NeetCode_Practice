def is_all_even(nums):
    for n in nums:
        if n % 2 != 0:
            return False
    return True


# One-liner alternative

nums1 = [2, 4, 6, 8, 10]
nums2 = [2, 4, 6, 8, 9]
print(is_all_even(nums1))
print(is_all_even(nums2))

print(all([n % 2 == 0 for n in nums1]))
print(all([n % 2 == 0 for n in nums2]))

print(any([n % 2 == 0 for n in nums1]))
print(any([n % 2 == 0 for n in nums2]))


# deque.append is faster than list.append and it can work like list
