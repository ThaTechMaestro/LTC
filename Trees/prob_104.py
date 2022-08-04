'''
Question Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/


Reference Solution:
https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/345948/python3Maximum-Depth-of-Binary-Tree-recursively-and-iteratively-Python3
-> Check out the iterative solution next
--> Difference between bfs and dfs
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
                          
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)
        
        return max(l_depth, r_depth)+1
        
        
        
        