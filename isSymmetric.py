# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool

给定一个二叉树，检查它是否是镜像对称的。
        """
        return self.isMirror(root, root)

    def isMirror(self, l_root, r_root):
        if l_root is None and r_root is None:
            return True
        elif l_root is None or r_root is None:
            return False
        elif l_root.val == r_root.val:
            return self.isMirror(l_root.left, r_root.right) and self.isMirror(l_root.right, r_root.left)
        else:
            return False
