# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
c1 = ListNode(1)
c2 = ListNode(2)
c3 = ListNode(3)
c4 = ListNode(4)
c1.next = c2
c2.next = c3
c3.next = c4
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        a = head
        b = head.next
        new_head = b
        if not b:
            return head
        while a:
            if a.next:
                p1 = a.next.next
            if p1 and p1.next:
                p2 = b.next.next
            else:
                p2 = None
            if p2:
                a.next = p2
                b.next = a
            else:
                a.next = p1
                b.next = a
                break
            a = p1
            b = p2
        return new_head


qwe = Solution()
print(qwe.swapPairs(c1).next.next.val)


# class Solution:
#     def swapPairs(self, head):
#         if head==None:
#             return None
#         else:
#             r1=head
#             r2=head
#             r2=r2.next
#             result=r2
#         if r2==None:
#             return head
#         else:
#             while r1.next.next!=None:
#                 mdi1=r1.next.next
#                 mdi2=r2.next.next
#                 r2.next=r1
#                 if mdi2==None:
#                     r1.next=mdi1
#                     return result
#                 else:
#                     r1.next=mdi2
#                     r1=mdi1
#                     r2=mdi2
#                     r2.next=r1
#                     r1.next=None
#         return result
