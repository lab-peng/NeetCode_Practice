from collections import deque
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def graph(self):
        current = self
        while current:
            print(str(current.val) + ' -> ', end='')
            current = current.next
        print('null')


def list_to_link(lst):
    cur = dummy = ListNode()
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        206. Reverse Linked List
        """
        current = head
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev


print('#1 206. Reverse Linked List')
head = list_to_link([1, 2, 3, 4, 5])
head.graph()
s = Solution()
reversed_list = s.reverseList(head)
reversed_list.graph()


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        21. Merge Two Sorted Lists
        """
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next


print('#2 21. Merge Two Sorted Lists')
list1, list2 = list_to_link([1, 2, 4]), list_to_link([1, 3, 4])
list1.graph()
list2.graph()
s = Solution()
merged_list = s.mergeTwoLists(list1, list2)
merged_list.graph()


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        143. Reorder List
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # divide the list into two and reverse second half
        second = slow.next
        prev = slow.next = None  # division into two halves
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # merge two halves
        first, second = head, prev
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2


print('#3 143. Reorder List')
head = list_to_link([1, 2, 3, 4, 5])
head.graph()
s = Solution()
s.reorderList(head)
head.graph()


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        19. Remove Nth Node From End of List
        """

        # # NeetCode solution
        # dummy = ListNode(0, head)
        # left, right = dummy, head
        # while n > 0:
        #     right = right.next
        #     n -= 1
        #
        # while right:
        #     left = left.next
        #     right = right.next
        # left.next = left.next.next
        # return dummy.next

        # slow, fast pointer solution
        slow, fast = head, head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


print('#4 19. Remove Nth Node From End of List')
head, n = list_to_link([1, 2, 3, 4, 5]), 2
# head, n = list_to_link([1, 2]), 1
# head, n = list_to_link([1]), 1
head.graph()
s = Solution()
final_head = s.removeNthFromEnd(head, n)
final_head.graph()


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        141. Linked List Cycle
        """
        slow, fast = head, head

        while fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


print('#5 141. Linked List Cycle')
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
# head.graph()
s = Solution()
print(s.hasCycle(head))


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        23. Merge k Sorted Lists
        """

        def merge(l1, l2):
            dummy = ListNode()
            current = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            if l1:
                current.next = l1
            if l2:
                current.next = l2
            return dummy.next

        if not lists[0]:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(merge(l1, l2))
            lists = merged_lists

        return lists[0]

        # if not lists:
        #     return None
        # if len(lists) == 1:
        #     return lists[0]
        #
        # if len(lists) == 2:
        #     l1, l2 = lists
        #     return merge(l1, l2)
        #
        # m = len(lists) // 2
        # l = self.mergeKLists(lists[:m])
        # r = self.mergeKLists(lists[m:])
        #
        # return merge(l, r)


print('#6 23. Merge k Sorted Lists:')
lists = [list_to_link([1, 4, 5]), list_to_link([1, 3, 4]), list_to_link([2, 6])]
for l in lists:
    l.graph()
s = Solution()
ans = s.mergeKLists(lists)
ans.graph()
