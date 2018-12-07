#!/usr/bin/env python3
from string import ascii_lowercase


def react(polymer):
    length = 0
    while len(polymer) != length:
        length = len(polymer)
        for letter in ascii_lowercase:
            polymer = polymer.replace(f"{letter}{letter.upper()}", '')
            polymer = polymer.replace(f"{letter.upper()}{letter}", '')
    return polymer


if __name__ == '__main__':
    with open('input.txt', 'r') as polyfile:
        polymer = polyfile.read().strip()
    length = len(react(polymer))
    for letter in ascii_lowercase:
        pruned = polymer.replace(letter, '').replace(letter.upper(), '')
        length = min(length, len(react(pruned)))
    print(length)
