from typing import List, Optional
from binary_tree import TreeNode, list_to_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


node_list = [4, 2, 7, 1, 3, 6, 9]
root = list_to_tree(node_list)
root.graph()
s = Solution()
inverted_root = s.invertTree(root)
inverted_root.graph()


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


s = Solution()
print(s.maxDepth(root))


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        572. Subtree of Another Tree
        """

        def is_same_tree(q, t):
            if not q and not t:
                return True
            if q and t and q.val == t.val:
                return is_same_tree(q.left, t.left) and is_same_tree(q.right, t.right)
            return False

        if not root:
            return False
        if is_same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


root = list_to_tree([3, 4, 5, 1, 2])
subRoot = list_to_tree([4, 1, 2])

root = list_to_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
subRoot = list_to_tree([4, 1, 2])
s = Solution()
print(s.isSubtree(root, subRoot))


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        235. Lowest Common Ancestor of a Binary Search Tree
        """
        # level order traversal


s = Solution()
root, p, q = list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), 2, 8
root.graph()

