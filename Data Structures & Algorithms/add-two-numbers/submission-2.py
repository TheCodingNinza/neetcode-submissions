# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2

        if not l2:
            return l1

        head = ListNode()
        previous = head
        carry = 0
        while True:
            if l1 and l2:
                previous.next = ListNode((l1.val + l2.val + carry) % 10)
                carry = int((l1.val + l2.val + carry) / 10)
                l1 = l1.next
                l2 = l2.next
            elif not l1 and l2:
                previous.next = ListNode((l2.val + carry) % 10)
                carry = int((l2.val + carry) / 10)
                l2 = l2.next
            elif not l2 and l1:
                previous.next = ListNode((l1.val + carry) % 10)
                carry = int((l1.val + carry) / 10)
                l1 = l1.next
            else:
                if carry != 0:
                    previous.next = ListNode(carry)
                break
            previous = previous.next

        temp = head.next
        head.next = None
        head = temp

        return head                