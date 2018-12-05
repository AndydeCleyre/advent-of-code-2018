#!/usr/bin/env python3
from sys import exit


def match(id1, id2):
    return sum(a != b for a, b in zip(id1, id2)) == 1


with open('input.txt', 'r') as idfile:
    box_ids = idfile.readlines()
    for i, box_id in enumerate(box_ids):
        for other_id in box_ids[i + 1:]:
            if match(box_id, other_id):
                print(''.join(c for i, c in enumerate(box_id) if other_id[i] == c))
                exit()
