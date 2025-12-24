# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        # length of linkedlist
        length = 0
        node = head
        while node:
            length=length+1
            node = node.next
        # check valid k
        k = k%length
        if k == 0:
            return head
        
        fast = head
        slow= head
        
        # Move fast pointer by K places

        while k>0:
            fast = fast.next
            k = k-1

        # Move fast and slow pointer until you reach last node

        while fast.next:
            fast = fast.next
            slow = slow.next
        # Manipulate pointer and return the list
        
        fast.next = head
        head = slow.next
        slow.next = None
        return head
        