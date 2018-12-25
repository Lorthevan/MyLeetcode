# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, x=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # recursive
        if l1 is None and l2 is None:
            return

        l1.val += l2.val + x
        x, l1.val = divmod(l1.val, 10)

        if x and l1.next is None:
            l1.next = ListNode(0)

        if l1.next or l2.next:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)

        self.addTwoNumbers(l1.next, l2.next, x)
        return l1

        # # Non - recursive
        # result = ListNode(0)
        # carry = 0
        # point = result
        #
        # while l1 or l2 or carry:
        #     val1 = (l1.val if l1 else 0)
        #     val2 = (l2.val if l1 else 0)
        #     carry, res = divmod(val1+val2+carry, 10)
        #
        #     point.next = ListNode(res)
        #     point = point.next
        #     l1 = (l1.next if l1 else None)
        #     l2 = (l2.next if l2 else None)
        #
        # return result