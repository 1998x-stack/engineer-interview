#!/usr/bin/env python3
"""Tiny experiment: modulo hashing vs consistent hashing remapping.
Educational only; not a production client implementation.
"""
import bisect, hashlib

def h(s: str) -> int:
    return int.from_bytes(hashlib.md5(s.encode()).digest()[:8], 'big')

def modulo(keys, nodes):
    return {k: nodes[h(k) % len(nodes)] for k in keys}

def ring_map(keys, nodes, replicas=100):
    ring=[]
    for node in nodes:
        for i in range(replicas): ring.append((h(f"{node}#{i}"), node))
    ring.sort(); points=[x[0] for x in ring]
    out={}
    for k in keys:
        pos=bisect.bisect_left(points,h(k))
        out[k]=ring[pos % len(ring)][1]
    return out

def remap(a,b): return sum(a[k]!=b[k] for k in a)/len(a)

if __name__=='__main__':
    keys=[f"key:{i}" for i in range(100_000)]
    a=[f"n{i}" for i in range(10)]; b=a+["n10"]
    print('modulo remap:', remap(modulo(keys,a), modulo(keys,b)))
    print('ring remap  :', remap(ring_map(keys,a), ring_map(keys,b)))
