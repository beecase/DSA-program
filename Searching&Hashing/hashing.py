class HashTable:
     def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

 # Hash function
     def hash_function(self, key):
        return key % self.size
 
 # Insert key into hash table
     def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)
 
 # Search key in hash table
     def search(self, key):
         index = self.hash_function(key)
         if key in self.table[index]:
                return True
         return False 
 # Display hash table
     def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i] ,"," , end= " ")

# Example
h = HashTable(10)
h.insert(17)
h.insert(20)
h.insert(15)
h.insert(7)
h.insert(32)
h.display()
print("\nSearch 15:", h.search(15))
print("Search 100:", h.search(100))