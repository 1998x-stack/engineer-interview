from __future__ import annotations
class Solution:
    def sortList(self, head: 'ListNode | None') -> 'ListNode | None':
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
        mid = slow.next; slow.next = None
        a, b = self.sortList(head), self.sortList(mid)
        dummy = tail = ListNode()
        while a and b:
            if a.val <= b.val: tail.next, a = a, a.next
            else: tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next
