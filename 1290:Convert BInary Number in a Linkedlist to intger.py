# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # s = [str(i) for i in head]
        # k = ("".join(s))
        # return (int(k,2))
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        a = 0
        for i in range(len(arr)):
            if arr[i]==1:
                a += 2**(len(arr)-1-i)
        return a
