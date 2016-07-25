# https://leetcode.com/problems/validate-binary-search-tree/

# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.
import unittest
import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_valid_bst(root):

    def is_valid_bst_impl(root, minimum, maximum):
        if not root:
            return True
        if not minimum < root.val < maximum:
            return False

        left_valid = is_valid_bst_impl(root.left, minimum, root.val) if root.left else True
        right_valid = is_valid_bst_impl(root.right, root.val, maximum) if root.right else True

        return left_valid and right_valid

    return is_valid_bst_impl(root, -sys.maxint, sys.maxint)


class ValidateBstTest(unittest.TestCase):

    def test_positive(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)

        self.assertTrue(is_valid_bst(root))

    def test_negative(self):
        root = TreeNode(10)
        root.left = TreeNode(15)
        root.right = TreeNode(5)

        self.assertFalse(is_valid_bst(root))

    def test_negative_with_left_tree(self):
        #     15
        #    /
        #   10
        #  /  \
        #  5  12
        #     /
        #    3 <- illegal, less than 5
        root = TreeNode(15)
        root.left = TreeNode(10)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(12)
        root.left.right.left = TreeNode(3)

        self.assertFalse(is_valid_bst(root))

    def test_negative_with_right_tree(self):
        #     15
        #    /  \
        #   10  18
        #       / \
        #      9
        #       \
        #        19 <- illegal, greater than 18
        root = TreeNode(15)
        root.left = TreeNode(10)
        root.right = TreeNode(18)
        root.right.left = TreeNode(9)
        root.right.left.right = TreeNode(19)

        self.assertFalse(is_valid_bst(root))


if __name__ == '__main__':
    unittest.main()