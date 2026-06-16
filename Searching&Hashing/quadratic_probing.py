class QuadraticProbingTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size

    def insert(self,key):
        hash_val=key%self.size
        for i in range(self.size):
            idx=(hash_val+i*i)%self.size
            if self.table[idx] is None:
                self.table[idx]=key
                return True
        return False
    
    def search(self,key):
        hash_val=key%self.size
        for i in range(self.size):
            idx=(hash_val+i*i)%self.size
            if self.table[idx]==key:
                return idx
            if self.table[idx] is None:
                break
        return -1
    
#Example Usage
if __name__ == "__main__":
 qp_table = QuadraticProbingTable(10)
 qp_table.insert(15)
 qp_table.insert(25) # Collision
 print(f"Quadratic Probing: 25 found at index {qp_table.search(25)}")