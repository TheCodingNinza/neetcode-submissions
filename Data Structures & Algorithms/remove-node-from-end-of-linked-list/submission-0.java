/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode firstPointer = head;
        ListNode secondPointer = head;
        int count = 0;
        while(count < n){
            secondPointer = secondPointer.next;
            count++;
        }
        if(secondPointer == null){
            head = head.next;
            return head;
        }else{
            while(secondPointer.next != null){
                firstPointer = firstPointer.next;
                secondPointer = secondPointer.next;
            }
            firstPointer.next = firstPointer.next.next;
            return head;
        }
    }
}
