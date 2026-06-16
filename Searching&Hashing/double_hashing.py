class DoubleHashingTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size

    def _hash(self,key):
        #Secondary hash must never return 0 and should 
        return 7-(key%7)
    
    def insert (self,key):
        h1=key %self.size
        step=self._hash(key)
        for i in range(self.size):
            idx=(h1+i*step)%self.size
            if self.table[idx] is None:
                self.table[idx]=key
                return True
        return False
    
    def search(self,key):
        h1= key%self.size
        step= self._hash(key)
        for i in range(self.size):
            idx=(h1+i*step)%self.size
            if self.table[idx]==key:
                return idx
            if self.table[idx] is None:
                break
        return -1
    

# Example Usage:
if __name__ == "__main__":
 dh_table = DoubleHashingTable(10)
 dh_table.insert(10)
 dh_table.insert(20) # Collision
 print(f"Double Hashing: 20 found at index {dh_table.search(20)}")