# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        # value값으로 비교? 
        stack = []

        # 2. 스택
        while cur :
            stack.append(cur.val)
            cur = cur.next
        
        cur = head

        while cur:
            if stack.pop() != cur.val:
                return False
            cur = cur.next
        
        return True