# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pointer = head
        for i in range(n):
            pointer = pointer.next
        if pointer is None:
            return head.next
        
        pointer_prev = head
        while pointer and pointer.next:
            pointer = pointer.next
            pointer_prev = pointer_prev.next
        
        target = pointer_prev.next
        if target:
            pointer_prev.next = target.next
            target.next = None
        else:
            pointer_prev = None
        return head