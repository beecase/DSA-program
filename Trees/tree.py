from typing import Optional, Any

class TreeNode:
    """
    A fundamental buliding block for Binary trees.
    """
    def __init__(self,value):
        self.value=value
        self.left = None
        self.right=None

    def __repr__(self) -> str:
        return f"Node(self.value)"
    

root=TreeNode(10)
root.left= TreeNode(5)
root.right= TreeNode(15)
    
print(f'Root:{root.value}')
print(f'Left Child:{root.left.value}')
print(f'Right Child:{root.right.value}')
    

    




