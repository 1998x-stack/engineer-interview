from __future__ import annotations
class Solution:
    def reverseKGroup(self, head: 'ListNode | None', k: int) -> 'ListNode | None':
        dummy = ListNode(0, head); group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth: return dummy.next
            group_next = kth.next
            prev, cur = group_next, group_prev.next
            while cur is not group_next:
                nxt = cur.next; cur.next = prev; prev, cur = cur, nxt
            old_start = group_prev.next
            group_prev.next = kth
            group_prev = old_start
