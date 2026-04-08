# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        itr = head
        while itr != None:
            if itr in visited:
                return True
            else:    
                visited.add(itr)
            itr = itr.next
        return False    
        