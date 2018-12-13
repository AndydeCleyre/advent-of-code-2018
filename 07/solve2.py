#!/usr/bin/env python3
from string import ascii_uppercase
from itertools import count
from collections import defaultdict


def solve(filename='input.txt', workers=5, base_time=60, all_steps=ascii_uppercase):
    ready_workers = workers
    todo = {step: set() for step in all_steps}
    with open(filename, 'r') as infile:
        for line in infile:
            todo[line.split()[7]].add(line.split()[1])
    finish_at = defaultdict(set)
    elapsed = count()
    for second in elapsed:
        try:
            done = finish_at.pop(second)
        except KeyError:
            pass
        else:
            for done_step in done:
                ready_workers += 1
                for step, deps in todo.items():
                    deps.discard(done_step)
        if todo:
            for worker in range(ready_workers):
                try:
                    next_up = min(step for step, deps in todo.items() if not deps)
                except ValueError:
                    pass
                else:
                    finish_at[second + ascii_uppercase.index(next_up) + base_time + 1].add(next_up)
                    del todo[next_up]
                    ready_workers -= 1
        else:
            return max(finish_at) if finish_at else second


if __name__ == '__main__':
    # print(solve('sample.txt', workers=2, base_time=0, all_steps='ABCDEF'))
    print(solve())
