# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def depth(root):
            if not root:
                return 0
            
            if not root.left:
                return 1 + depth(root.right)

            if  not root.right:
                return 1 + depth(root.left)

            return 1 + min(depth(root.left), depth(root.right))
        
        return depth(root)