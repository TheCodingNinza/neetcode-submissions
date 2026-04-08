# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        
        if not list2:
            return list1    
        
        head = None
        itr1 = None
        itr2 = None

        if list1.val <= list2.val:
            head = list1
            itr1 = list1
            itr2 = list2
        else:
            head = list2
            itr1 = list2
            itr2 = list1

        while True:
            if itr1.next == None:
                itr1.next = itr2
                break
            elif itr2 == None:
                break    
            elif itr1.next.val > itr2.val:
                temp1 = itr1.next
                itr1.next = itr2
                temp2 = itr2.next
                itr2.next = temp1
                itr1 = itr2
                itr2 = temp2
            elif itr1.next.val <= itr2.val:    
                itr1 = itr1.next

        return head        