from __future__ import annotations
class Solution:
    def reverseList(self, head: 'ListNode | None') -> 'ListNode | None':
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        return prev
