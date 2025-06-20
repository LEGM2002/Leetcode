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
        ListNode support = new ListNode(0); //this node will help us to add the new ones
        ListNode current = support; //to always keep on the last added node
        int extra = 0; //to store 1 if the sum are greater than 9
        while(l1 != null || l2 != null || extra == 1){
            int sum = 0;
            if(l1 != null){
                sum += l1.val;
                l1 = l1.next; //pass to the next node
            }
            if(l2 != null){
                sum += l2.val;
                l2 = l2.next;
            }
            sum += extra;
            extra = sum / 10; //store only 0 or 1
            current.next = new ListNode(sum % 10); //module to store the second digit if the number has two digits
            current = current.next; //pass to the added node
        }
        return support.next; //we don't need the first node
    }
}