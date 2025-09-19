from collections import deque

class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_cousins(self, root, x, y):
    
    def get_depth_and_parent(node, target):
        queue = deque([(root, 0, None)]) #node, depth, parent
        
        while queue:
            curr,depth,parent= queue.popleft()
            
            if curr.val == target:
                return (depth, parent)
            
            if curr.left:
                queue.append(curr.left, depth+1, curr)
            
            if curr.right:
                queue.append(curr.right, depth+1, curr)
        
        return None,None

    x_depth, x_parent = get_depth_and_parent(root,x)
    y_depth, y_parent = get_depth_and_parent(root, y)
    
    return (x_depth==y_depth) and (x_parent==y_parent)


        
        
         
        
    