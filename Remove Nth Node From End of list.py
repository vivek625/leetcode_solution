# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return None
        ptr = head
        ct = 0
        while (ptr != None):
            ct += 1
            ptr = ptr.next
        p = ct - n
        if p == 0:
            head = head.next
            return head
        ct = 1
        ptr = head
        while (ct < p):
            ptr = ptr.next
            ct += 1
        ptr.next = ptr.next.next
        return head
