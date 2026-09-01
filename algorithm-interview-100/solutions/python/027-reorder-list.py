from __future__ import annotations
class Solution:
    def reorderList(self, head: 'ListNode | None') -> None:
        if not head or not head.next: return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next; fast = fast.next.next
        second = slow.next; slow.next = None
        prev = None
        while second:
            nxt = second.next; second.next = prev; prev, second = second, nxt
        first, second = head, prev
        while second:
            n1, n2 = first.next, second.next
            first.next = second; second.next = n1
            first, second = n1, n2
