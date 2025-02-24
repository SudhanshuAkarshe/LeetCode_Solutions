# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if  not head or k==0  or not head.next:
            return head
        count = 1
        first = head
        while first.next:
            count+=1
            first = first.next
        first.next = head
        
        k = k % count
        count = count - k
        tail = head
        for _ in range(count-1):
            tail = tail.next
        
        
        head = tail.next
        tail.next = None
        return head


        