# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # current = head
        # prev = None
        # while current:
        #     next_ = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_
        # return prev
        
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        next_ = head.next
        next_.next = head
        head.next = None
        return new_head