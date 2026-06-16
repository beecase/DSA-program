class Node:
    """"
    A single node ina a doubly linked list."""
    def _init_(self,data):
        """
        Initializes the node with data and null pointer
        """
        self.data=data
        self.next= None #Pointer to next node
        self.prev=None #Pointer to previous node
    def _repr_(self):
        """
        PROVIDES A HELPFUL STRING REPRESENTAION FOR PRINTING
        """
        return str(self.data)