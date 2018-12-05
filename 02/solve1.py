#!/usr/bin/env python3
from collections import Counter


twins, triplets = 0, 0
with open('input.txt', 'r') as box_ids:
    for box_id in box_ids:
        freqs = Counter(box_id).values()
        twins += bool(2 in freqs)
        triplets += bool(3 in freqs)
print(twins * triplets)
