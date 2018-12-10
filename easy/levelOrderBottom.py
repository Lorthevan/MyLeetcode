# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        stack = [root]
        result = []
        while len(stack) > 0:
            cache = []
            per_list = []
            for item in stack:
                if item.left:
                    cache.append(item.left)
                if item.right:
                    cache.append(item.right)
                per_list.append(item.val)
            result.insert(0, per_list)
            stack = cache
        
        return result
