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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0)
            return null;
        List<ListNode> validList = new ArrayList<>();
        for(int i=0;i<lists.length;i++){
            if(lists[i] != null){
                validList.add(lists[i]);
            }
        }    
        if(validList.size() == 0)
            return null;
        ListNode head = validList.get(0);
        ListNode itr = head;
        
        for(int i=0;i<validList.size()-1;i++){
            while(itr.next != null){
                itr = itr.next;
            }
            itr.next = validList.get(i+1);
        }
        if(head == null)
            return head;
        List<ListNode> arr = new ArrayList<>();
        ListNode iterator = head;
        
        while(iterator != null){
            arr.add(iterator);
            iterator = iterator.next;
        }

         Collections.sort(arr, new Comparator<ListNode>() {
            public int compare(ListNode a, ListNode b) {
                return Integer.compare(a.val, b.val);
            }
        });

        for(int i=0;i<arr.size()-1;i++){
            arr.get(i).next = arr.get(i+1);
        }
        
        arr.get(arr.size()-1).next = null;

        return arr.get(0);
    }
}
