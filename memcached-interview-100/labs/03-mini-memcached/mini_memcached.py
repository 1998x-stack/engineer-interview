#!/usr/bin/env python3
"""A deliberately small cache core for interview study.
Implements TTL + LRU semantics using Python containers; it is NOT Memcached-compatible.
"""
from collections import OrderedDict
from dataclasses import dataclass
import time
from typing import Optional

@dataclass
class Item:
    value: bytes
    expire_at: Optional[float]

class MiniMemcached:
    def __init__(self, capacity: int = 1024):
        self.capacity = capacity
        self.data: OrderedDict[str, Item] = OrderedDict()

    def set(self, key: str, value: bytes, ttl: int = 0) -> None:
        expire_at = time.time() + ttl if ttl > 0 else None
        self.data.pop(key, None)
        self.data[key] = Item(value, expire_at)
        self.data.move_to_end(key, last=False)
        while len(self.data) > self.capacity:
            self.data.popitem(last=True)

    def get(self, key: str) -> Optional[bytes]:
        item = self.data.get(key)
        if item is None:
            return None
        if item.expire_at is not None and time.time() >= item.expire_at:
            del self.data[key]
            return None
        self.data.move_to_end(key, last=False)
        return item.value

    def delete(self, key: str) -> bool:
        return self.data.pop(key, None) is not None

if __name__ == '__main__':
    c=MiniMemcached(capacity=2)
    c.set('foo', b'bar', ttl=1)
    assert c.get('foo') == b'bar'
    time.sleep(1.05)
    assert c.get('foo') is None
    print('ok')
