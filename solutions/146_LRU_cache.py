# https://leetcode.com/problems/lru-cache/

from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        assert capacity > 0
        self.capacity = capacity
        self.cache = {}
        self.last_accessed = deque()

    def get(self, key: int) -> int:
        try:
            result = self.cache.get(key)
            self.last_accessed.remove(key)
            self.last_accessed.appendleft(key)
        except:
            result = -1
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.last_accessed:
            self.cache[key] = value
            self.last_accessed.remove(key)
            self.last_accessed.appendleft(key)
        else:
            if len(self.last_accessed)==self.capacity:
                evict_key = self.last_accessed.pop()
                del self.cache[evict_key]
            self.cache[key] = value
            self.last_accessed.appendleft(key)