# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        currentNode = head.next
        previousNode = head

        while currentNode:
            temp = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = temp

        head.next = None
        return previousNode       