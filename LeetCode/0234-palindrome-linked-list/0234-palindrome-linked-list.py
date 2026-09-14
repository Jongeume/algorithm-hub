# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        prev = None
        next_tmp = None
        fast = cur
        slow = cur
        is_even = False

        while fast.next :
            if fast.next.next is None : 
                fast = fast.next
                is_even = True
            else :
                fast = fast.next.next
            slow = slow.next
        
        # back : slow -> fast
        # front:  <- slow

        while cur is not slow:
            next_tmp = cur.next
            cur.next = prev
            prev = cur
            cur = next_tmp 

        if not is_even:
            cur = cur.next

        while cur :
            if cur.val != prev.val :
                return False
            cur = cur.next
            prev = prev.next    
        
        return True

    