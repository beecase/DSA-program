class BinarySearch:
    @staticmethod
    def find_first(sorted_data, target):
        """Locates the first occurrence in O(log n) time."""
        low, high = 0, len(sorted_data) - 1
        result = -1

        while low <= high:
            mid = low + (high - low) // 2

            if sorted_data[mid] == target:
                result = mid
                high = mid - 1   # search left side
            elif sorted_data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result

    @staticmethod
    def find_last(sorted_data, target):
        """Locates the last occurrence in O(log n) time."""
        low, high = 0, len(sorted_data) - 1
        result = -1

        while low <= high:
            mid = low + (high - low) // 2

            if sorted_data[mid] == target:
                result = mid
                low = mid + 1   # search right side
            elif sorted_data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result

    @classmethod
    def find_all(cls, sorted_data, target):
        """Locates all occurrences using first and last index."""
        first = cls.find_first(sorted_data, target)

        if first == -1:
            return []

        last = cls.find_last(sorted_data, target)
        return list(range(first, last+1))
    
data=[2,7,7,10,12,32]
print("FIRST OCCURANCE:",BinarySearch.find_first(data,7))
print("LAST OCCURANCE:",BinarySearch.find_last(data,7))
print("FIRST OCCURANCE:",BinarySearch.find_all(data,7))