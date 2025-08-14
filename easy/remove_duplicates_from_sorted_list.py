# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def remove_duplicates(self, head):
        # number of nodes [0, 300]
        # always on ascending order
        current = head # start in the first node
        while current and current.next: # avoid index out of bounds
            if current.val == current.next.val:
                # jump the duplicate node
                current.next = current.next.next
            else:
                # keep the next node that has a different value
                current = current.next
        return head

        