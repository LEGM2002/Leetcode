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
        ListNode first = head;
        ListNode last = head;
        if(head == null){  //empty list
            return null;
        }
        for(int i = 0; i < n; i++){ //move n positions in front of last 
            first = first.next;
        }
        if(first == null){  //nth node is the first node
            return head.next;
        }
        while(first.next != null){   //first arrive to the last position
            first = first.next;
            last = last.next;
        }
        last.next = last.next.next; //remove nth node from the end
        return head;
    }
}