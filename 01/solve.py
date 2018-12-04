#!/usr/bin/env python3
if __name__ == '__main__':
    with open('input.txt', 'r') as numfile:
        print(sum(map(int, numfile)))
