from threading import RLock

class ThreadSafeCache:
    def __init__(self, capacity, eviction_policy):
        self.capacity = capacity
        self.store = dict()
        self.lock = RLock()
        self.eviction_policy = eviction_policy

    def get(self, key):
        with self.lock:
            if key in self.store:
                self.eviction_policy.key_accessed(key)
                return self.store[key]
            return None

    def put(self, key, value):
        with self.lock:
            if key in self.store:
                self.store[key] = value
                self.eviction_policy.key_accessed(key)
            else:
                if len(self.store) >= self.capacity:
                    evict_key = self.eviction_policy.evict()
                    if evict_key is not None:
                        self.store.pop(evict_key, None)
                        self.eviction_policy.key_removed(evict_key)
                self.store[key] = value
                self.eviction_policy.key_added(key)

    def remove(self, key):
        with self.lock:
            if key in self.store:
                del self.store[key]
                self.eviction_policy.key_removed(key)
