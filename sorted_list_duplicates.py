# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import unittest


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = []

        prev_val = None
        current = head
        after = head.next if head else None

        while current:
            prev_val = prev_val & 0xffffffff if prev_val is not None else None
            current_val = current.val & 0xffffffff
            after_val = after.val & 0xffffffff if after else None

            is_current_strictly_increasing = (current == head or prev_val < current_val) and\
                                             (not after or current_val < after_val)

            is_current_strictly_decreasing = (current == head or prev_val > current_val) and\
                                             (not after or current_val > after_val)

            if is_current_strictly_increasing or is_current_strictly_decreasing:
                new_list.append(ListNode(current.val))

            prev_val = current.val
            current = after
            after = after.next if after else None

        for i in xrange(0, len(new_list) - 1):
            new_list[i].next = new_list[i + 1]

        return new_list[0] if new_list else None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class RemoveDuplicatesTest(unittest.TestCase):

    def convert_node_to_list(self, node):
        actual_list = []
        while node:
            actual_list.append(node.val)
            node = node.next
        return actual_list

    def test_remove_duplicates(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)

        actual_list = self.convert_node_to_list(Solution().deleteDuplicates(head))

        self.assertEquals(actual_list, [1, 3])

    def test_remove_duplicates_two_dupes_in_a_row(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(3)
        head.next.next.next.next.next = ListNode(4)

        actual_list = self.convert_node_to_list(Solution().deleteDuplicates(head))

        self.assertEquals(actual_list, [1, 4])

    def test_remove_duplicates_from_head(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)

        actual_list = self.convert_node_to_list(Solution().deleteDuplicates(head))

        self.assertEquals(actual_list, [2, 3])

    def test_remove_empty_head(self):
        head = None

        actual_list = self.convert_node_to_list(Solution().deleteDuplicates(head))

        self.assertEquals(actual_list, [])

    def test_descending_order(self):
        head = ListNode(2)
        head.next = ListNode(1)

        actual_list = self.convert_node_to_list(Solution().deleteDuplicates(head))

        self.assertEquals(actual_list, [2, 1])

    def test_descending_order_with_dupe(self):
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(1)

        actual_list = self.convert_node_to_list(Solution().deleteDuplicates(head))

        self.assertEquals(actual_list, [3, 1])

    def test_remove_singular_head(self):
        head = ListNode(1)

        actual_list = self.convert_node_to_list(Solution().deleteDuplicates(head))

        self.assertEquals(actual_list, [1])

    def test_integer_bounds(self):
        head = ListNode(-2147483648)
        head.next = ListNode(2147483647)
        head.next.next = ListNode(2)

        actual_list = self.convert_node_to_list(Solution().deleteDuplicates(head))

        self.assertEquals(actual_list, [-2147483648, 2147483647, 2])

    def test_none_unique(self):
        head = ListNode(0)
        head.next = ListNode(0)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(0)
        head.next.next.next.next = ListNode(0)

        actual_list = self.convert_node_to_list(Solution().deleteDuplicates(head))

        self.assertEquals(actual_list, [])

if __name__ == '__main__':
    unittest.main()