from typing import Optional

class BSTNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    # Insert
    def insert(self, key: int) -> None:
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node: Optional[BSTNode], key: int) -> BSTNode:
        if not node:
            return BSTNode(key)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)

        return node

    # Search
    def search(self, key: int) -> bool:
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: Optional[BSTNode], key: int) -> bool:
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    # Delete
    def delete(self, key: int) -> None:
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node: Optional[BSTNode], key: int) -> Optional[BSTNode]:
        if not node:
            return None

        # Find node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Case 1 & 2: one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Case 3: two children
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)

        return node

    def _min_value_node(self, node: BSTNode) -> BSTNode:
        current = node
        while current.left:
            current = current.left
        return current


#EXAMPLE USAGE
if __name__ == "__main__":
    bst = BinarySearchTree()

    elements = [50, 30, 20, 40, 70, 60, 80]
    print("Inserting elements:", elements)

    for x in elements:
        bst.insert(x)

    print("Searching for 40:", bst.search(40))  # True
    print("Searching for 90:", bst.search(90))  # False

    print("\nDeleting 20 (Leaf Node)...")
    bst.delete(20)
    print("Searching for 20:", bst.search(20))  # False

    print("\nDeleting 30 (Node with one/two child)...")
    bst.delete(30)
    print("Searching for 30:", bst.search(30))  # False