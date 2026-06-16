from collections import deque
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
    

class BFS:

    @staticmethod
    def breadth_first_search(root:Optional[TreeNode]) -> List[Any]:
        """
        BFS: Level-by-level traversal using a Queue
        Also known as Level Order Traversal.

        Time Complexity :0(N)
        Space Complexity :0(W) where W is the maximum width
        """
        if not root:
            return []
        
        result = []
        # We use deque as a Queue (FIFO)
        queue = deque([root])

        while queue:
            # 1. Dequeue the front node
            current = queue.popleft() # O(1) operation

            # 2. Process/Visit the node
            result.append(current.value)

            # 3. Enqueue children for next level processing
            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
                
        return result
        
 

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

    
    print(f"Breadth First Search:{BFS.breadth_first_search(root)}")
