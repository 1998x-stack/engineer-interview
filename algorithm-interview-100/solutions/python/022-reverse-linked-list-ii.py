from __future__ import annotations
class Solution:
    def reverseBetween(self, head: 'ListNode | None', left: int, right: int) -> 'ListNode | None':
        dummy = ListNode(0, head)
        pre = dummy
        for _ in range(left - 1): pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            move = cur.next
            cur.next = move.next
            move.next = pre.next
            pre.next = move
        return dummy.next
