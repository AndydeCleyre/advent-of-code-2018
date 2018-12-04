#!/usr/bin/env python3

class Claim:

    def __init__(self, id, x, y, width, height):
        self.id = id
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
    claims, claimed, overclaimed = set(), set(), set()
    with open('input.txt', 'r') as claimfile:
        for line in claimfile:
            id, _, anchor, size = line.split()
            id = id.lstrip('#')
            x, y = map(int, anchor.rstrip(':').split(','))
            width, height = map(int, size.split('x'))
            claim = Claim(id, x, y, width, height)
            claims.add(claim)
            cells = claim.cells
            overclaimed |= (claimed & cells)
            claimed |= cells
    for claim in claims:
        if not (claim.cells & overclaimed):
            print(claim.id)
            break
