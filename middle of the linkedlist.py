# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # s = []
        # h = math.floor(len(arr)/2)
        # for i in range(h,len(arr)):
        #     s.append(arr[i])
        # print(s)
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
    
