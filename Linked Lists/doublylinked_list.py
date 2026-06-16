class Node:
    """"
    A single node ina a doubly linked list."""
    def __init__(self,data):
        """
        Initializes the node with data and null pointer
        """
        self.data=data
        self.next= None #Pointer to next node
        self.prev=None #Pointer to previous node
    def __repr__(self):
        """
        PROVIDES A HELPFUL STRING REPRESENTAION FOR PRINTING
        """
        return str(self.data)
    
    
class DoublyLinkedList:
    """ 
    A wrapper class for a doubly linked list
    Maintains head and tail for 0(1) end operations.
      """
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    
    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        return self.count
    
    def _repr_(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "None <-->" + "<-->" .join(nodes)+"<-->None"
    
    def traverse_forward(self):
        """
        Prints all values from head to tail.
        Analysis: 0(n) time,0(n) space.
        """
        print("DLL Forward",end=" ")
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print("None")

    def traverse_reverse(self):
        """Prints all values in the list (backward). O(n) time."""
        print("DLL (Reverse):", end=' ')
        current = self.tail
        while current:
            print(current.data, end=' <-> ')
            current = current.prev
        print("None")

    def insert_at_beginning(self, data):
        """Inserts a new node at the front of the list O(1) time."""
        new_node = Node(data)
        self.count += 1
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node # Link old head's prev to new node
            self.head = new_node      # Set new node as head
    
    def insert_at_end(self, data):
        """Inserts a new node at the end of the list. O(1) time with tail pointer."""
        new_node = Node(data)
        self.count += 1
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail # Link new node's prev to old tail
            self.tail.next = new_node # Link old tail's next to new node
            self.tail = new_node      # Set new node as tail

    def insert_after_node(self, prev_node, data):
        """Insert a new node after a given node. O(1) time if node reference is known."""
        if not prev_node:
            print("Error: Previous node is None.")
            return 
        # If inserting after the tail, use insert_at_end for tail update
        if prev_node == self.tail:
             self.insert_at_end(data)
             return
             
        new_node = Node(data)
        
        new_node.next = prev_node.next 
        new_node.prev = prev_node
        
        prev_node.next.prev = new_node # Link the node after prev_node back to new_node
        prev_node.next = new_node
        
        self.count += 1

    def delete_at_beginning(self):
        """Deletes the head node and returns its data. O(1) time."""
        if self.is_empty():
            print("Error: List is empty.")
            return None
        
        node_to_delete = self.head
        self.count -= 1

        if self.head == self.tail: # Only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None # Detach new head's prev pointer
            
        return node_to_delete.data

    def delete_at_end(self):
        """Delete the last node and returns its data. O(1) time for DLL (due to prev pointer)."""
        if self.is_empty():
            print("Error: List is empty")
            return None

        node_to_delete = self.tail
        self.count -= 1
        
        if self.head == self.tail: # Only one node
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev # Move tail back one
            self.tail.next = None       # Detach new tail's next pointer
            
        return node_to_delete.data
    
    def delete_by_key(self, key):
        """Deletes the first node with the given key. O(n) time."""
        current = self.head

        while current:
            if current.data == key:
                data = current.data
                self.count -= 1
                
                if current == self.head:
                    # Deleting the head
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None # List became empty
                elif current == self.tail:
                    # Deleting the tail
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    # Deleting a middle node
                    current.prev.next = current.next
                    current.next.prev = current.prev
                
                return data
            current = current.next
            
        print(f"Error: key '{key}' not found in list")


# Create a new doubly linked list
dll = DoublyLinkedList()

# Insert elements at the end
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

# Insert elements at the beginning
dll.insert_at_beginning(5)
dll.insert_at_beginning(2)

# Traverse forward
dll.traverse_forward()   

# Traverse in reverse
dll.traverse_reverse()   
# Insert after a given node 
print("Inserting 3 after head node:")
dll.insert_after_node(dll.head, 3)
dll.traverse_forward()   

# Delete at beginning
print("After deleting the beginning node:")
dll.delete_at_beginning()  
dll.traverse_forward()      

# Delete at end
print("After deleting the end node:")
dll.delete_at_end()         
dll.traverse_forward()      

# Delete by key
print("Deleting node 10 :")
dll.delete_by_key(10)      
dll.traverse_forward()      

