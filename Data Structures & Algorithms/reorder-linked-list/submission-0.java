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
    public void reorderList(ListNode head) {
        if(head == null || head.next == null)
            return;
        ListNode current = head;
        ListNode tail = head;
        while(tail.next.next != null){
            tail = tail.next;
        }
        while(current != tail && current.next != null){
            ListNode temp = current.next;
            tail.next.next = temp;
            current.next = tail.next;
            tail.next = null;
            tail = head;
            while(tail.next.next != null){
                tail = tail.next;
            }
            current = temp;
        }
    }
}
