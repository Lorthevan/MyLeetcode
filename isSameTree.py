# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
        """
        # if p and q:
        #     if p.val == q.val:
        #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        #     else:
        #         return False
        # elif not p and not q:
        #     return True
        # else:
        #     return False
# 逻辑优化:边界条件提前
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


