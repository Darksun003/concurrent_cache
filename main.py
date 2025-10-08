from cache.cache import ThreadSafeCache
from cache.lru_policy import LRUEvictionPolicy

if __name__ == "__main__":
    cache = ThreadSafeCache(2, LRUEvictionPolicy())
    cache.put("a", 1)
    cache.put("b", 2)
    print(cache.get("a"))  # should return 1
    cache.put("c", 3)      # evicts "b"
    print(cache.get("b"))  # should return None
