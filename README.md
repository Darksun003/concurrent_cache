CONCURRENT THREAD-SAFE CACHE WITH PLUGGABLE EVICTION POLICIES
Overview
This project implements a high-performance, thread-safe in-memory cache supporting concurrent read and write operations. It is designed to allow multiple threads to safely interact with the cache simultaneously without data corruption or performance degradation.

A key feature of this cache is pluggable eviction policies, enabling dynamic configuration of how entries are removed when the cache reaches its maximum capacity. Supported eviction policies include:

Least Recently Used (LRU)

Least Frequently Used (LFU)

Features
Thread-Safe Cache Core: Supports concurrent get(key) and put(key, value) operations using appropriate synchronization mechanisms.

Pluggable Eviction Policies: Abstract eviction interface with concrete implementations for LRU and LFU policies.

Dynamic Eviction: Automatically evicts cache entries based on the configured policy when capacity is exceeded.

Benchmarking: Performance benchmarks comparing eviction policies under concurrent load.

Testing: Unit tests validating correctness and thread safety.

Project Structure
```
concurrent_cache/
│
├── cache/
│   ├── __init__.py
│   ├── cache.py                 # Core cache implementation (ThreadSafeCache)
│   ├── eviction_policy.py       # EvictionPolicy interface and implementations (LRU, LFU)
│
├── benchmarks/
│   ├── __init__.py
│   ├── benchmark.py             # Benchmark scripts comparing eviction policies
│
├── tests/
│   ├── __init__.py
│   ├── test_cache.py            # Unit and concurrency tests
│
├── main.py                     # Example usage script
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── design_summary.txt          # Design decisions and architecture summary
└── performance_report.txt      # Analysis of concurrency and performance results
```
Design Summary
See design_summary.txt for an overview of architecture, synchronization mechanisms, and data structures used.

Performance Report
See performance_report.txt for detailed concurrency and performance analysis comparing the eviction policies.

Extensibility
New eviction policies can be added by implementing the EvictionPolicy abstract base class.

Cache capacity and eviction policy can be configured dynamically.

Synchronization can be fine-tuned for different workloads.

License
Specify your project license here (e.g., MIT License).****
