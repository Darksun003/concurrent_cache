from abc import ABC, abstractmethod
from collections import OrderedDict, defaultdict

# Abstract base class
class EvictionPolicy(ABC):
    @abstractmethod
    def key_accessed(self, key):
        """Called when a key is accessed (read/write)."""
        pass

    @abstractmethod
    def key_added(self, key):
        """Called when a new key is added."""
        pass

    @abstractmethod
    def evict(self):
        """Returns the key to evict."""
        pass

    @abstractmethod
    def key_removed(self, key):
        """Called when a key is removed."""
        pass


# LRU Policy Implementation
class LRUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.order = OrderedDict()

    def key_accessed(self, key):
        if key in self.order:
            self.order.move_to_end(key)

    def key_added(self, key):
        self.order[key] = None
        self.order.move_to_end(key)

    def evict(self):
        return next(iter(self.order)) if self.order else None

    def key_removed(self, key):
        if key in self.order:
            del self.order[key]


# LFU Policy Implementation
class LFUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.freq = defaultdict(int)

    def key_accessed(self, key):
        self.freq[key] += 1

    def key_added(self, key):
        self.freq[key] = 1

    def evict(self):
        return min(self.freq, key=self.freq.get) if self.freq else None

    def key_removed(self, key):
        if key in self.freq:
            del self.freq[key]
