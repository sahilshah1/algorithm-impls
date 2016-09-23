# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []

        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        dummy = None
        head = None
        while heap:
            val = heapq.heappop(heap)
            if not head:
                head = ListNode(val)
                dummy = ListNode(0)
                dummy.next = head
            else:
                head.next = ListNode(vaL)
                head = head.next

        return dummy.next if dummy else None
