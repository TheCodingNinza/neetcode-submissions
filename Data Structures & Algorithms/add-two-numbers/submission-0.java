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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        int carryForward = 0;
        ListNode itr1 = l1, itr2 = l2, itr = null;
        ListNode head = null;
        int flag = 0;

        while (true){

            int val1 = itr1 != null ? itr1.val : 0;
            int val2 = itr2 != null ? itr2.val : 0;
            int val = (val1 + val2 + carryForward) % 10;
            carryForward = (val1 + val2 + carryForward) / 10;
            ListNode newNode = new ListNode(val);
            if( flag == 0){
                head = newNode;
                itr = newNode;
                flag = 1;
            }else{
                itr.next = newNode;
                itr = itr.next;
            }
            itr1 = itr1 != null ? itr1.next : null;
            itr2 = itr2 != null ? itr2.next : null;

            if(itr1 == null && itr2 == null){
                break;
            }

        }

        if(carryForward != 0){
            ListNode newNode = new ListNode(carryForward);
            itr.next = newNode;
        }

//        head = reverseIt(head);
        return head;

    }
}
