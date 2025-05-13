# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        aset = set()
        if not head:
            return False
        t = head
        while t.next:
            if t.next in aset:
                return True
            aset.add(t.next)
            t = t.next
        return False

        