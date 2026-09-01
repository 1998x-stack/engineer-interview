from __future__ import annotations
import heapq

class Solution:
    def mergeKLists(self, lists: list['ListNode | None']) -> 'ListNode | None':
        heap = []
        for i, node in enumerate(lists):
            if node: heapq.heappush(heap, (node.val, i, node))
        dummy = tail = ListNode()
        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node; tail = node
            if node.next: heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
