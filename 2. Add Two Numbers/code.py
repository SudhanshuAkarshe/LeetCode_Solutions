# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
       
        num1 = 0
        num2 = 0
        c1 = 0
        c2 = 0
        while l1:
            num1+=l1.val * (10**c1)
            c1+=1
            l1 = l1.next

        while l2:
            num2+=l2.val * (10**c2)
            c2+=1
            l2 = l2.next
      
        s = list(str(num1+num2))
        head = ListNode(int(s[-1]))
        current = head
        for ele in s[-2::-1]:
            current.next = ListNode(int(ele))
            current = current.next

        return head
      