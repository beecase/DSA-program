class Node:
    """"
    A single node ina a singly linked list."""
    def __init__(self,data):
        """
        Initializes the node with data and null pointer
        """
        self.data=data
        self.next= None
    def __repr__(self):
        """
        PROVIDES A HELPFUL STRING REPRESENTAION FOR PRINTING
        """
        return str(self.data)




       
