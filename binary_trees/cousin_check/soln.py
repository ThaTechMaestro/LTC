from collections import deque

def is_cousin(root, x, y):
    """
    Check if two nodes in a binary tree are cousins.
    
    Two nodes are cousins if they are at the same level but have different parents.
    
    :return: True if the nodes are cousins, False otherwise.
    
    Using 2 Simpler implementations:
        f

    """
    
    
  
            
    # Placeholder for the actual implementation
    pass

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