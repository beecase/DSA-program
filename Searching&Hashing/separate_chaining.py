class SeparateChainingTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key):
        index = key % self.size
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        index = key % self.size
        return key in self.table[index]


# Example Usage:
if __name__ == "__main__":
    sc_table= SeparateChainingTable(5)
    sc_table.insert(10)
    sc_table.insert(15) # Both hash to index 0
    print(f"Separate Chaining: 15 found? {sc_table.search(15)}")