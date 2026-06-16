class LinearProbingTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
    
    def insert(self,key):
        index= key%self.size
        for i in range(self.size):
            probe_idx=(index+i)%self.size
            if self.table[probe_idx] is None:
                self.table[probe_idx]=key
                return True
        return False
    
    def search(self,key):
        index=key%self.size
        for i in range(self.size):
            probe_idx=(index+i)%self.size
            if self.table[probe_idx]==key:
                return probe_idx
            if self.table[probe_idx] is None:
                break
        return -1
    
#Example Usage

if __name__=="__main__":
    lp_table=LinearProbingTable(10)
    lp_table.insert(12)
    lp_table.insert(22)
    print(f"Linear Probing:22 found at index {lp_table.search(22)}")
