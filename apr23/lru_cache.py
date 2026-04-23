from collections import OrderedDict

class LRUCache:
    def __init__(self, cap):
        self.cache = OrderedDict()
        self.cap = cap

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

c = LRUCache(2)
c.put(1,10)
c.put(2,20)
print(c.get(1))