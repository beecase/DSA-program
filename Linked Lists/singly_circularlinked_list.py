class Node:
    """Node for Singly Circular Linked List"""
    def __init__(self,data):
        self.data=data
        self.next=None
    
class SinglyCircularLinkedList:
    def __init__(self):
        """Initialize an empty SCLL with only a 'last' pointer."""
        self.last=None
        self.count=0
    
    def is_empty(self):
        return self.last is None
    
    def __len__(self):
        return self.count

    def insert_at_beginning(self, data):
        new_node = Node(data)
        self.count += 1

        if self.is_empty():
            self.last = new_node
            new_node.next = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node  # Head updated
            
    def insert_at_end(self,data):
        """Inserts at the end.0(1)."""
        new_node=Node(data)
        self.count+=1

        if self.is_empty():
            self.last=new_node
            new_node.next=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node
            self.last=new_node
    
    def delete_by_key(self,key):
        """Deletes a node bu a key. Returns True if deleted else False"""
        if self.is_empty():
            return False
        prev=self.last
        current=self.last.next #head

        for  _ in range(self.count):
            if current.data==key:
                #1. Only node in list
                if self.count==1:
                    self.last=None
                else:
                    #Link past the removed node
                    prev.next=current.next
                    #update last if needed
                    if current== self.last:
                        self.last=prev
                    self.count-=1
                    return True
                
                prev=current
                current=current.next
              
        return False # Not found
    
    def traverse(self):
        """Prints the list in circular order."""
        if self.is_empty():
            print("SCLL: Empty")
            return
    
        print("SCLL:", end=" ")
        current = self.last.next
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.last.next:
                break
        
        print(f"back to {current.data}")

    def to_list(self):
        """Return a python list with circular order"""
        if self.is_empty():
            return []
        
        result = []
        current =self.last.next
        while True:
            result.append(current.data)
            current=current.next
            if current==self.last.next:
                break
        return result
#Illustrate test cases for singlycircularlinked list
if __name__=="__main__":
    print("\n Insert at the end into empty list")
    s=SinglyCircularLinkedList()
    s.insert_at_end(10)
    print("Expected:[10] (single node pointing to itself)")
    print("Actual:",s.to_list())

    print("\n Insert at beginning into NON-empty list")
    s.insert_at_beginning(5)
    print("Expected;[5,10]")
    print("Actual:",s.to_list())

    print("\n Insert at end into NON-Empty list:")
    s.insert_at_end(20)
    print("Expected: [5,10,20]")
    print("Actual: ", s.to_list())

    print("\nDelete HEAD (5)")
    s.delete_by_key(5)
    print("Expected: [10,20] (new head = 10)")
    print("Actual: ", s.to_list())

    print("\nTraverse demonstration")
    s.traverse()
          
        
            
