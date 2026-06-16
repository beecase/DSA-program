class HashTable:
    def __init__(self, size, method="linear"):
        self.size = size
        self.table = [None] * size
        self.method = method  # linear, quadratic, or double

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return 7 - (key % 7)  # Used for double hashing

    def probe(self, key, i):
        h = self.hash1(key)
        if self.method == "linear":
            return (h + i) % self.size
        elif self.method == "quadratic":
            return (h + i * i) % self.size
        elif self.method == "double":
            return (h + i * self.hash2(key)) % self.size

    def insert(self, key):
        for i in range(self.size):
            idx = self.probe(key, i)
            if self.table[idx] is None:
                self.table[idx] = key
                return True
        return False

    def search(self, key):
        for i in range(self.size):
            idx = self.probe(key, i)
            if self.table[idx] == key:
                return idx
            if self.table[idx] is None:
                break
        return -1

    def display(self):
        print(self.table)


# Example Usage
if __name__ == "__main__":
    print("Linear Probing")
    linear = HashTable(10, "linear")
    linear.insert(12)
    linear.insert(22)
    print("22 found at index:", linear.search(22))
    linear.display()

    print("\nQuadratic Probing")
    quad = HashTable(10, "quadratic")
    quad.insert(15)
    quad.insert(25)
    print("25 found at index:", quad.search(25))
    quad.display()

    print("\nDouble Hashing")
    double = HashTable(10, "double")
    double.insert(10)
    double.insert(20)
    print("20 found at index:", double.search(20))
    double.display()