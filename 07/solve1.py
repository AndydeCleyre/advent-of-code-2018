#!/usr/bin/env python3
from string import ascii_uppercase


if __name__ == '__main__':
    with open('input.txt', 'r') as infile:
        steps = set((line.split()[1], line.split()[7]) for line in infile)
    todo = ascii_uppercase
    ordered = ''
    while todo:
        first = min(set(todo) - set(step[1] for step in steps))
        ordered += first
        todo = todo.replace(first, '')
        for step in tuple(steps):
            if step[0] == first:
                steps.remove(step)
    print(ordered)
