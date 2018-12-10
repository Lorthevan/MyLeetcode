# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        # 按前序遍历规则,找到最下层的不含左子树的节点,然后回到上一层
        if root.left is None:
            return
            
        # 找到左子树的最深右子树
        l = root.left
        while l.right:
            l = l.right
        
        # 修改指向
        l.right = root.right
        root.right = root.left
        root.left = None
