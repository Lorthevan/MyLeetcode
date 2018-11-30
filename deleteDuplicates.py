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
        给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
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
