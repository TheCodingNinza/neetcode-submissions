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
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null)
            return head;
        ListNode tail = head;
        while(tail.next.next != null){
            tail = tail.next;
        }
        ListNode temp = tail;
        tail = tail.next;
        ListNode headForReversedList = tail;
        tail.next = temp;
        tail = tail.next; 
        while(tail.next != head){
             ListNode itr = head;
             while(itr.next != tail.next){
                itr = itr.next;
             }
             tail.next = itr;
             tail = tail.next;
        }
        head.next = null;
        return  headForReversedList;

    }
}
