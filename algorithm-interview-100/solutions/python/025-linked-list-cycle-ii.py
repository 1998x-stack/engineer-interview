from __future__ import annotations
class Solution:
    def detectCycle(self, head: 'ListNode | None') -> 'ListNode | None':
        slow = fast = head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
            if slow is fast:
                p = head
                while p is not slow:
                    p = p.next; slow = slow.next
                return p
        return None
