
from typing import Optional, Any,List

class TreeNode:
    """
    A fundamental buliding block for Binary trees.
    """
    def __init__(self,value):
        self.value=value
        self.left = None
        self.right=None

    def __repr__(self) -> str:
        return f"Node({self.value})"
    
class DFSTraversal:
    """
    Static methods for recursive Depth-first Search traversals.UnicodeTranslateError.
        
    """

    @staticmethod
    def preorder(node:Optional[TreeNode]) -> List[Any]:
        """Root -> Left -> Right"""
        if not node:
            return[]
        return [node.value] + DFSTraversal.preorder(node.left)+DFSTraversal.preorder(node.right)
   
    @staticmethod
    def inorder(node:Optional[TreeNode]) -> List[Any]:
        """Left -> Root -> Right"""
        if not node:
            return[]
        return  DFSTraversal.inorder(node.left)+[node.value]+DFSTraversal.inorder(node.right)
    
    @staticmethod
    def postorder(node:Optional[TreeNode]) -> List[Any]:
        """Left -> Right -> Root"""
        if not node:
            return[]
        return  DFSTraversal.inorder(node.left)+DFSTraversal.inorder(node.right)+[node.value]
    
    
if __name__ == "__main__":
    """
    Constructing Tree:
                    1
                 /     \
                2       3
               /
              4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    print(f"DFS Preorder: {DFSTraversal.preorder(root)}")
    print(f"DFS Inorder: {DFSTraversal.inorder(root)}")
    print(f"DFS Postorder: {DFSTraversal.postorder(root)}")
    