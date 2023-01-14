import copy


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def graph(self):
        """Graph an instance of (tree) Node class"""
        lines, *_ = self.graph_aux()
        for line in lines:
            print(line)

    def graph_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = str(self.val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.graph_aux()
            s = str(self.val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.graph_aux()
            s = str(self.val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.graph_aux()
        right, m, q, y = self.right.graph_aux()
        s = str(self.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def height(self):
        return self._TreeNode__height(self)

    def __height(self, root):
        if not root:
            return 0
        return 1 + max(self.__height(root.left), self.__height(root.right))

    # Height and Depth are the same thing, if we consider the root node
    def depth(self):
        return self.height()

    # #  It doesn't work don't know why
    # def is_balanced(self):
    #     return self._TreeNode__is_balanced(self)
    #
    # def __is_balanced(self, root):
    #     if not root:
    #         return True
    #     if abs(self.__height(root.left) - self.__height(root.left)) > 1:
    #         return False
    #     return self.__is_balanced(root.left) and self.__is_balanced(root.right)

    def size(self):
        return TreeNode.__size(self)

    @staticmethod
    def __size(root):
        if not root:
            return 0
        return 1 + TreeNode.__size(root.left) + TreeNode.__size(root.right)

    def invert(self):
        TreeNode.__invert(self)

    @staticmethod
    def __invert(root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        TreeNode.__invert(root.left)
        TreeNode.__invert(root.right)


def list_to_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()













# r1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
#
# r1.left = n2
# r1.right = n3
# # n2.left = n4
# # n2.right = n5
# n3.left = n6
# n3.right = n7
# n7.left = TreeNode(8)
#
# r2 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
#
# r2.left = n2
# r2.right = n3
# n2.left = n4
# n2.right = n5
# n3.left = n6
# n3.right = n7
#
# print('The Graph of R1: ')
# r1.graph()
# print('The Graph of R2: ')
# r2.graph()
# print('R1 Height: ', r1.height())
# print('R1 Depth: ', r1.depth())
# print('R1 Size: ', r1.size())


def is_same_tree(p, q):
    if not p and not q:
        return True
    if not (p and q and p.val == q.val):
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# print('R1 and R2 are the same tree: ', is_same_tree(r1, r2))
#
# r1.invert()
# print('R1 after r1.invert(): ')
# r1.graph()
#
# r1.invert()
# print('R1 after r1.invert() again: ')
# r1.graph()


def inverted(root):
    root = copy.copy(root)
    if not root:
        return None
    root.left, root.right = root.right, root.left
    inverted(root.left)
    inverted(root.right)
    return root


# r3 = inverted(r1)  # This will change tree r1, too
# print('Original R1 Graph: ')
# r1.graph()
# print('inverted(R1) Graph: ')
# r3.graph()


def is_balanced(root):
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    if not root:
        return True
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


# print(is_balanced(r1))


def min_depth(root):
    if not root:
        return 0
    left_depth = min_depth(root.left)
    right_depth = min_depth(root.right)
    if not left_depth or not right_depth:
        return max(left_depth, right_depth) + 1
    return min(left_depth, right_depth) + 1


# print(min_depth(r1))
