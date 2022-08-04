'''
Question Link: 
https://leetcode.com/problems/minimum-depth-of-binary-tree/


Reference Solution:
https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/629657/Python-O(n)-by-DFS-and-BFS-85%2B-w-Comment


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        elif not root.left:
            return self.minDepth(root.right) + 1
        
        elif not root.right:
            return self.minDepth(root.left) + 1
        
        else:
            l_depth = self.minDepth(root.left)
            r_depth = self.minDepth(root.right)
            
            return min(l_depth, r_depth) + 1
        
    
        
