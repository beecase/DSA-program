class LinearSearch: 
    def __init__(self,array, key, mode= 'first'):
        self.array = array
        self.key = key    
        if mode == 'first':
            self._linear_search_first(array,key)
        elif mode == 'all':
            self._linear_search_all(array,key)
        else:
            raise ValueError("Mode must be \"first\" or \"all\"")

    #For first ocuurance 
    def _linear_search_first(self,array,key):
        #Returns first occurance of search key in a given array
        for index,value in enumerate(self.array):
            if value == self.key:
                return index
        return -1 

    #For multiple occurance
    def _linear_search_all(self, array, key):
        #Returns all occurance of search key in a given array
        searched_indices = []
        for index, value in enumerate(self.array):
            if value == self.key:
                searched_indices.append(index)
        
        return searched_indices   
        
array = [4,2,3,5,2,1,2]
key = 2
linear_search = LinearSearch(array, key, mode= 'first')
print("First Occurance:",linear_search._linear_search_first(array,key))

linear_search_all = LinearSearch(array, key, mode ='all')
print("Total Occurance:",linear_search_all._linear_search_all(array,key))
