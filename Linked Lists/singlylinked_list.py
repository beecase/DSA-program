from singly_node import Node
# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Traversal
    def traverse(self):
        current = self.head
        if current is None:
            print("List is empty")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Insertion at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insertion at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert after a given value
    def insert_after(self, prev_value, data):
        temp = self.head

        while temp:
            if temp.data == prev_value:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

        print("Value not found in list")

    # Retrieval
    def search(self, key):
        temp = self.head
        position = 1

        while temp:
            if temp.data == key:
                return position
            temp = temp.next
            position += 1

        return -1

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete by value
    def delete_value(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next


