# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         vals = list()
#         pointer = head = ListNode(None)
#
#         for nodes in lists:
#             while nodes:
#                 vals.append(nodes.val)
#                 nodes = nodes.next
#         for x in sorted(vals):
#             pointer.next = ListNode(x)
#             pointer = pointer.next
#         return head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            print(lists[0])
            return lists[0]
        if len(lists) == 0:
            return lists
        
        nodes = self.mergeTwoLists(lists.pop(), lists.pop())
        lists.append(nodes)
        self.mergeKLists(lists)
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = l_head = ListNode(None)
        
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
            l = l.next
        
        l.next = l1 or l2
        return l_head.next
