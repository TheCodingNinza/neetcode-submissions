# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head
         
        if not head.next:
            return
        
        while True:
            right = head
            while right.next.next:
                right = right.next
            if left.val == right.val or right.next.val == left.val:
                break     
            temp = left.next
            left.next = right.next
            right.next = None
            left = left.next
            left.next = temp
            left = left.next
        
              
