from __future__ import annotations
class Solution:
    def copyRandomList(self, head: 'Node | None') -> 'Node | None':
        if not head: return None
        cur = head
        while cur:
            copy = Node(cur.val, cur.next)
            cur.next = copy; cur = copy.next
        cur = head
        while cur:
            if cur.random: cur.next.random = cur.random.next
            cur = cur.next.next
        dummy = tail = Node(0); cur = head
        while cur:
            copy = cur.next; cur.next = copy.next
            tail.next = copy; tail = copy; cur = cur.next
        return dummy.next
