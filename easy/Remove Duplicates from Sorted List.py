# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        a = head
        b = head.next
        while a and b:
            if a.val == b.val:
                a.next = b.next
                b = a.next
            else:
                a = b
                b = b.next
        return head
