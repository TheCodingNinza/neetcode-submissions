# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        tail = head

        while tail.next:
            tail = tail.next

        initHead = head
        head = tail

        while tail != initHead:
            itr = initHead

            while itr.next != tail:
                itr = itr.next

            tail.next = itr
            tail = itr


        tail.next = None

        return head       