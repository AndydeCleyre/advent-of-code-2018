#!/usr/bin/env python3

class Claim:

    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height

    @property
    def cells(self):
        return set(
            (x, y)
            for x in range(self.x, self.x + self.width)
            for y in range(self.y, self.y + self.height)
        )


if __name__ == '__main__':
    claimed, overclaimed = set(), set()
    with open('input.txt', 'r') as claimfile:
        for line in claimfile:
            _, _, anchor, size = line.split()
            x, y = map(int, anchor.rstrip(':').split(','))
            width, height = map(int, size.split('x'))
            cells = Claim(x, y, width, height).cells
            overclaimed |= (claimed & cells)
            claimed |= cells
    print(len(overclaimed))
