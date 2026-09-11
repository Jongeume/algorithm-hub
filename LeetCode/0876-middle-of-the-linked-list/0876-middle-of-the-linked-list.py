# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        slow = cur
        fast = cur

        while fast.next:
            slow = cur.next
            if fast.next.next is None:
                fast = fast.next
            else :
                fast = fast.next.next
            cur = cur.next
        
        head = slow
        return  head