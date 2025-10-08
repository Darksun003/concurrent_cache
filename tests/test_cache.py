import threading
import time
from cache.cache import ThreadSafeCache
from cache.lru_policy import LRUEvictionPolicy

def test_concurrent_access():
    cache = ThreadSafeCache(3, LRUEvictionPolicy())

    def writer():
        for i in range(10):
            cache.put(f'key{i}', f'value{i}')
            time.sleep(0.01)

    def reader():
        for i in range(10):
            val = cache.get(f'key{i}')
            print(f"Read {val}")
            time.sleep(0.01)

    threads = [threading.Thread(target=writer), threading.Thread(target=reader)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    test_concurrent_access()
