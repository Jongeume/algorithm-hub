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

        # None이 왜 안될까
        
        while fast.next :
            slow = slow.next
            if fast.next.next is None:
                fast = fast.next
            else:
                fast = fast.next.next

        cur = slow
        return cur
    
