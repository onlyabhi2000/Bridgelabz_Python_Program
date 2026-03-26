"""
self.order keeps the usage order of keys

self.cache holds the actual key → value mappings

If the cache is full, we remove from the front (least used)

When a key is used or updated, we move it to the end


"""


from collections import deque

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def get(self, key):
        if key not in self.cache:
            return -1
        
        # if present then move it to to the end ( most recently used)

        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]
    
    def put(self, key , value):
        #    # If key already exists, remove it first
        if key in self.cache:
            #update the value and move it to the end 
            self.order.remove(key)
             #if key is full and and key is new , remove the least recently used item
        elif len(self.cache) == self.capacity:
            lru = self.order.popleft()
            del self.cache[lru]

        #add the key to the end (most recently used ) and store its value
        self.order.append(key)           
        self.cache[key] = value
            

lru = LRUCache(3)
lru.put(1 , 'A')
lru.put(2 , 'B')
lru.put(3 , 'C')
print(lru.get(2))

lru.put(4, 'D')
print(lru.cache)

print(list(lru.order))