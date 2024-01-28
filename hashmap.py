class HashTable:  
    def __init__(self):
        #size of table
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        #get the index in memory with asc numbers
        #SUM of asc numbers from table and use mod the sum %
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        #get item from hash
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        #set item in hash
        h = self.get_hash(key)
        self.arr[h] = val  

    def __delitem__(self, key):
        #set item in hash
        h = self.get_hash(key)
        self.arr[h] = None  


hashtable = HashTable()
print(hashtable.get_hash('test 1'))
hashtable['test 1'] = "test 1 value"
print(hashtable.arr)

del hashtable['test 1']
print(hashtable.arr)