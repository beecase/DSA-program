class Node:
    """Node for Doubly Circular Linked List"""
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class DoublyCircularLinkedList:
    def __init__(self):
        """Initializes an empty DCLL using only a 'head' pointer.
        The tail is availiable as self.head.prev whem list is non empty
        """
        self.head=None
        self.count=0


    def is_empty(self):
        return self.head is None
    

    def __len__(self):
        return self.count
    

    def insert_at_beginning(self,data):
        new_node=Node(data)
        self.count+=1

        if self.is_empty():
            #Single node-> points to itself both ways
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            tail=self.head.prev

            new_node.next=self.head
            new_node.prev=tail

            self.head.prev=new_node
            tail.next=new_node

            self.head= new_node #new head
    

    def insert_at_end(self,data):
        new_node=Node(data)
        self.count+=1

        if self.is_empty():
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            tail=self.head.prev

            new_node.next=self.head
            new_node.prev=tail

            tail.next=new_node
            self.head.prev= new_node
            #Note: head doesnot change

    
    def traverse(self):
        if self.is_empty():
            print("DCLL:Empty")
            return
        
        print("DCLL:",end=" ")
        current=self.head

        while True:
            print(current.data,end="<->")
            current=current.next
            if current==self.head:
                break
        print(f"(back to {current.data})")

# Create an empty doubly circular linked list
dcll = DoublyCircularLinkedList()

# Insert at beginning
dcll.insert_at_beginning(10)
dcll.insert_at_beginning(5)

# Insert at end
dcll.insert_at_end(20)
dcll.insert_at_end(30)

# Traverse the list
dcll.traverse()  
print("\nExpected Output: DCLL: 5<->10<->20<->30<->(back to 5)")

# Insert another at beginning
dcll.insert_at_beginning(2)
dcll.traverse()  
print("\nExpected: DCLL: 2<->5<->10<->20<->30<->(back to 2)")

# Insert another at end
dcll.insert_at_end(40)
dcll.traverse()  
print("\nExpected: DCLL: 2<->5<->10<->20<->30<->40<->(back to 2)")

# Print count
print("Length:", len(dcll))  




