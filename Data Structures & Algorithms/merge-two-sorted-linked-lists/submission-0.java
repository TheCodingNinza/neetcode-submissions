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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode pointer1 = list1;
        ListNode pointer2 = list2;
        if(list1 == null)
            return list2;

        if(list2 == null)
            return list1;    
        
        // if(list1.val <= list2.val){
            ListNode basePointer = list1.val <= list2.val ? list1 : list2;
            ListNode movablePointer = list1.val <= list2.val ? list2 : list1;
            while(movablePointer != null){
                // System.out.println("basePointer1: "+basePointer.val);
                // System.out.println("movablePointer: "+movablePointer.val);
                while(basePointer.next != null && basePointer.next.val <= movablePointer.val)
                    basePointer = basePointer.next;    
                // System.out.println("basePointer2: "+basePointer.val);    
                ListNode temp = basePointer.next;
                basePointer.next = movablePointer;
                movablePointer = temp;
            }
        // }

        return list1.val <= list2.val ? list1 : list2;
    }
}