from typing import List, Optional
from collections import deque
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
        current = root
        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current


s = Solution()
root, p, q = list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), TreeNode(2), TreeNode(8)
# root.graph()
print(s.lowestCommonAncestor(root, p, q).val)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        102. Binary Tree Level Order Traversal
        """
        ans = []
        q = deque([])
        if root:
            q.append(root)

        while q:
            lvl = []
            for i in range(len(q)):
                current = q.popleft()
                lvl.append(current.val)

                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            ans.append(lvl)
        return ans


root = list_to_tree([3, 9, 20, None, None, 15, 7])
# root.graph()

s = Solution()
print(s.levelOrder(root))


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        98. Validate Binary Search Tree
        """

        def dfs(lower, node, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            return dfs(lower, node.left, node.val) and dfs(node.val, node.right, upper)

        return dfs(float('-inf'), root, float('inf'))


root = list_to_tree([2, 1, 3])
root = list_to_tree([5, 1, 4, None, None, 3, 6])
# root.graph()
s = Solution()
print(s.isValidBST(root))


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        230. Kth Smallest Element in a BST
        """
        # TODO:  iterative inorder traversal not fully grasped
        counter = 1
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if counter == k:
                return current.val
            counter += 1
            current = current.right


root = list_to_tree([3, 1, 4, None, 2])
root = list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
k = 2
root.graph()
s = Solution()
print(s.kthSmallest(root, k))


# def preorder(root):
#     if not root:
#         return []
#     return [root.val] + preorder(root.left) + preorder(root.right)
# def inorder(root):
#     if not root:
#         return []
#     return inorder(root.left) + [root.val] + inorder(root.right)
# print(preorder(root))
# print(inorder(root))


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        105. Construct Binary Tree from Preorder and Inorder Traversal
        """
        if not preorder and not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: 1 + mid], inorder[:mid])
        root.right = self.buildTree(preorder[1 + mid:], inorder[mid+1:])
        return root


preorder, inorder = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
s = Solution()
s.buildTree(preorder, inorder).graph()


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        124. Binary Tree Maximum Path Sum
        :param root:
        :return:
        """


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))