/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        
        Node newHead = null;
        Node itr = head;
        Map<Node, Node> map = new HashMap<>();
        
        while(itr != null){
            Node temp = new Node(itr.val);
            map.put(itr, temp);
            if(itr == head)
                newHead = temp;
            itr = itr.next;
        }

        itr = head;

        while(itr != null){
            Node temp = map.get(itr);

            if(itr.next != null){
                temp.next = map.get(itr.next);
            }else{
                temp.next = null;
            }

            if(itr.random != null){
                temp.random = map.get(itr.random);
            }else{
                temp.random = null;
            }

            itr = itr.next;
        }

        return newHead;

    }
}
