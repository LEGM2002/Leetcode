# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def remove_duplicates(self, head):
        # number of nodes [0, 300]
        # always on ascending order
        current = head
        while current and current.next:
            if current.val == current.next.val:
                # jump the duplicate node
                current.next = current.next.next
            else:
                current = current.next
        return head

        