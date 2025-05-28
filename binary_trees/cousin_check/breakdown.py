from collections import deque

def print_level(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        current_level = []
        
        for _ in range(len(queue)):
            node = queue.popleft()
            current_level.append(str(node.val))
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        print(",".join(current_level))

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

if __name__=="__main__":
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n2 = TreeNode(2,left=n4)
    n3 = TreeNode(3, right=n5)
    root = TreeNode(1,left=n2, right=n3)
    
    print_level(root)


        
        