class TreeNode:
    """Node for Binary Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"

# Example Usage:
if __name__ == "__main__":
    # Root
    root = TreeNode(70)
    
    # Level 1
    root.left = TreeNode(60)
    root.right = TreeNode(50)
    
    # Level 2
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(30)
    root.right.left = TreeNode(20)
    root.right.right = TreeNode(10)

    # Printing nodes
    print("Root:", root.value)
    print("Left Child:", root.left.value)
    print("Right Child:", root.right.value)
    
    print("Left Left Child:", root.left.left.value)
    print("Left Right Child:", root.left.right.value)
    print("Right Left Child:", root.right.left.value)
    print("Right Right Child:", root.right.right.value)