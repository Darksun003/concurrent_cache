from collections import defaultdict
from threading import RLock
from .eviction_policy import EvictionPolicy

class LFUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.lock = RLock()
        self.freq_map = defaultdict(int)
        self.key_freq = {}

    def key_accessed(self, key):
        with self.lock:
            self.freq_map[key] += 1
            self.key_freq[key] = self.freq_map[key]

    def key_added(self, key):
        with self.lock:
            self.freq_map[key] = 1
            self.key_freq[key] = 1

    def evict(self):
        with self.lock:
            if not self.key_freq:
                return None
            return min(self.key_freq, key=lambda k: self.key_freq[k])

    def key_removed(self, key):
        with self.lock:
            self.freq_map.pop(key, None)
            self.key_freq.pop(key, None)
