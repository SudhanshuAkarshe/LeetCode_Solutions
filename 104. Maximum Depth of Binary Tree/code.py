# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        import math
        def depth(root):
            if not root:
                return 0
            
            return 1 + max(depth(root.left),depth(root.right))

        
        return depth(root)
        