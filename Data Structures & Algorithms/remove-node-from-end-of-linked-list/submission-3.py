# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        left = head
        right = head
        count = n
        while count > 1:
            right = right.next
            count -= 1
        while right.next != None:
            right = right.next
            left = left.next  
        previous = head
        if left == head:
            temp = head
            head = head.next
            temp.next = None
            
            return head
        
        while previous.next != left:
            previous = previous.next
        
        previous.next = left.next
        left.next = None 
        return head   