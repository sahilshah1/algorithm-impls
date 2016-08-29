# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# TODO: leet code solution just checks if p and q exist in the same subtree
import unittest

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_stack = find_node(root, p)
        q_stack = find_node(root, q)

        ancestor = None
        for i in xrange(0, min(len(p_stack), len(q_stack))):
            if p_stack[i] == q_stack[i]:
                ancestor = p_stack[i]
            else:
                break
        return ancestor


def find_node(root, target):
    def find_node_helper(n):
        stack.append(n)

        found = False

        if n == target:
            found = True

        if n.left and not found:
            found = find_node_helper(n.left)
        if n.right and not found:
            found = find_node_helper(n.right)

        if not found:
            stack.pop()

        return found

    stack = []
    find_node_helper(root)
    return stack


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LCABinaryTreeTest(unittest.TestCase):

    def test_find_node(self):
        #     15
        #    /
        #   10
        #  /  \
        #  5  12
        #     /
        #    3
        root = TreeNode(15)
        root.left = TreeNode(10)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(12)
        root.left.right.left = TreeNode(3)

        stack = map(lambda n: n.val, find_node(root, root.left.right.left))
        self.assertEquals(stack, [15, 10, 12, 3])

    def test_find_ancestor(self):
        #     15
        #    /
        #   10
        #  /  \
        #  5  12
        #     /
        #    3
        root = TreeNode(15)
        root.left = TreeNode(10)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(12)
        root.left.right.left = TreeNode(3)

        # find lca of 3 and 5 (10)
        lca = Solution().lowestCommonAncestor(root, root.left.left, root.left.right.left)
        self.assertEquals(lca, root.left)



if __name__ == '__main__':
    unittest.main()