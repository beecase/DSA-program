from typing import Optional

class AVLNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height = 1


class AVLTree:

    def get_height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def get_balance(self, node: Optional[AVLNode]) -> int:
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def _update_height(self, node: AVLNode) -> None:
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # Right Rotate
    def right_rotate(self, y: AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right

        # Rotation
        x.right = y
        y.left = T2

        # Update heights
        self._update_height(y)
        self._update_height(x)

        return x

    # Left Rotate
    def left_rotate(self, x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left

        # Rotation
        y.left = x
        x.right = T2

        # Update heights
        self._update_height(x)
        self._update_height(y)

        return y

    # Insert
    def insert(self, root: Optional[AVLNode], key: int) -> AVLNode:
        # 1. Normal BST insert
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # no duplicates

        # 2. Update height
        self._update_height(root)

        # 3. Balance factor
        balance = self.get_balance(root)

        # 4. Rotations

        # LL
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


#EXAMPLE USAGE
if __name__ == "__main__":
    avl = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]
    print("Inserting keys:", keys)

    for key in keys:
        root = avl.insert(root, key)

    # Checking structure
    print("\nRoot of AVL Tree:", root.key)
    print("Height of Root:", root.height)
    print("Root Left Child:", root.left.key)
    print("Root Right Child:", root.right.key)