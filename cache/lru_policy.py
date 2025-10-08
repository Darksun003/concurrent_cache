from collections import OrderedDict
from threading import RLock
from .eviction_policy import EvictionPolicy

class LRUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.lock = RLock()
        self.order = OrderedDict()

    def key_accessed(self, key):
        with self.lock:
            if key in self.order:
                self.order.move_to_end(key)

    def key_added(self, key):
        with self.lock:
            self.order[key] = None

    def evict(self):
        with self.lock:
            if self.order:
                return next(iter(self.order))
            return None

    def key_removed(self, key):
        with self.lock:
            self.order.pop(key, None)
