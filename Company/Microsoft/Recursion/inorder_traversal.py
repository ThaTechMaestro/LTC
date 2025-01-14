# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val 

    self.left=left
    self.right = right


class Solution:

  def inorder_traversal(self, root):

    result = []

    def inorder_trav_impl(root):

      if not root:
        return 

      inorder_trav_impl(root.left)
      result.append(root.val)
      inorder_trav_impl(root.right)


    inorder_trav_impl(root)
    return result

#----------> Test
first_node = Node(1)
second_node = Node(2)
third_node = Node(3)

first_node.left = None 
first_node.right = second_node
second_node.left = third_node

trav = Solution()

print(trav.inorder_traversal(first_node))
       
#---------------------Iterative Solution
def inorder_traversal(self, root):

  result = []
  stack = []

  while True:

    while root:
      stack.append(root.val)
      root = root.left
    
    if not stack:
      return result 
    
    node = stack.pop()
    result.append(node.val)
    root = node.right



