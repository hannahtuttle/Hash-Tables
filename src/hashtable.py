# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        out_put = (len(key) * 528) 
        # print(out_put)
        # return hash(key)
        return out_put


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        # print('testing index',idx)
        if self.storage[idx] is not None:
            temp = self.storage[idx]
            while temp.next is not None:
                if temp.key is key:
                    temp.value = value
                    # print(temp.value)
                    break
                temp = temp.next
            if temp.key is key and temp.value is value:
                pass
            elif temp.key is key and temp.value is not value:
                temp.value = value
            else:
                temp.next = LinkedPair(key, value)
        else:
            self.storage[idx] = LinkedPair(key, value)
        



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        current_node = self.storage[idx]
        previous_node = None
        while current_node.key is not key:
            if current_node.next is None and current_node.key is not Key:
                print('key does not exist')
                break
            previous_node = current_node
            current_node = current_node.next
        # print(current_node.key)
        if previous_node is not None:
            previous_node.next = current_node.next
            # print('checking change',previous_node.next.key)
        else:
            self.storage[idx] = None
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        current_node = self.storage[idx]
        # print(key)
        # self.storage[idx] = None
        # print(self.storage[idx])
        current_val = None
        if current_node is not None:
            while current_node.key is not key and current_node.next is not None:
                current_node = current_node.next
            # print(current_node.key)
            current_val = current_node.value
        return current_val


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        temp_storage = [None] * self.capacity
        for i in range(self.capacity // 2):
            temp_storage[i] = self.storage[i]
        self.storage = temp_storage

# h = HashTable(10)
# h._hash('hello')
# h._hash('hello world')



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
