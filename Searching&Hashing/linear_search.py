class LinearSearch:
    def __init__(self, array, key, mode):
        self.array = array
        self.key = key
        self.mode = mode.lower()

        if self.mode == "first":
            print("First occurrence index:", self.linear_search_first())
        elif self.mode == "last":
            print("Last occurrence index:", self.linear_search_last())
        elif self.mode == "all":
            indices = self.linear_search_all()
            print("All occurrence indices:", indices)
            print("Count:", len(indices))
        else:
            print("Invalid mode")


    def linear_search_first(self):
        for i, value in enumerate(self.array):
            if value == self.key:
                return i
        return -1


    def linear_search_last(self):
        last_index = -1
        for i, value in enumerate(self.array):
            if value == self.key:
                last_index = i
        return last_index


    def linear_search_all(self):
        searched_indices = []
        for i, value in enumerate(self.array):
            if value == self.key:
                searched_indices.append(i)
        return searched_indices


# Example usage
a = [1, 2, 3, 4, 5, 5, 6, 7, 3]

LinearSearch(a, 5, "first")
LinearSearch(a, 5, "last")
LinearSearch(a, 5, "all")
import numpy as np
np.random.seed(10)
