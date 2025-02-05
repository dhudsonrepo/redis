# Multi-Tier Cache System with Redis

This project implements a multi-tier cache system using Redis as the first-tier (in-memory) cache, disk-based caching as the second-tier, and a remote cache (API) as the third-tier.

## Features

- In-memory cache using Redis
- Disk cache as a fallback
- Remote cache using an API endpoint (can be replaced with a real service)
- Supports get, set, and delete operations across all tiers

## Requirements

- Python 3.x
- Redis server (local or remote)
- Disk space for cache files

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/dhudsonrepo/multi-tier-cache.git
    cd multi-tier-cache
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start Redis server on `localhost:6379` or configure the `config/settings.py` for a remote Redis server.


4. Run the tests:
    ```bash
    python -m unittest discover tests/
    ```

## Usage

You can interact with the cache system by using the `CacheSystem` class in `main.py`.

Example:
```python
from main import CacheSystem

cache = CacheSystem()
cache.set("user:123", "John Doe")
print(cache.get("user:123"))  # Output: John Doe
