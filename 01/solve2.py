#!/usr/bin/env python3
from itertools import cycle

freq = 0
history = set((0,))
with open('input.txt', 'r') as numfile:
    for line in cycle(numfile):
        freq += int(line)
        if freq in history:
            print(freq)
            break
        else:
            history.add(freq)
