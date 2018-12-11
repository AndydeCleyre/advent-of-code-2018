#!/usr/bin/env python3
from collections import defaultdict, Counter


class CoordBoard:

    def __init__(self, filename):
        with open(filename, 'r') as infile:
            self.coords = set(
                tuple(map(int, line.split(', ')))
                for line in infile
            )
        self.top_left = tuple(
            min(c[xy] for c in self.coords)
            for xy in (0, 1)
        )
        self.bottom_right = tuple(
            max(c[xy] for c in self.coords)
            for xy in (0, 1)
        )
        self.infinites = set(
            self.closest_coord(point)
            for point in self.perimeter_coords()
        )

    def get_lands(self):
        lands = Counter()
        for x in range(self.top_left[0], self.bottom_right[0] + 1):
            for y in range(self.top_left[1], self.bottom_right[1] + 1):
                coord = self.closest_coord((x, y))
                if coord and coord not in self.infinites:
                    lands[coord] += 1
        return lands

    def closest_coord(self, point):
        short_distances = defaultdict(set)
        shortest = None
        for coord in self.coords:
            dist = sum(abs(point[xy] - coord[xy]) for xy in (0, 1))
            if shortest is None or dist <= shortest:
                shortest = dist
                short_distances[dist].add(coord)
        if len(short_distances[shortest]) != 1:
            return None
        return short_distances[shortest].pop()

    def perimeter_coords(self):
        return set(  # top and bottom rows
            (x, y)
            for y in (self.top_left[1], self.bottom_right[1])
            for x in range(self.top_left[0], self.bottom_right[0] + 1)
        ) | set(  # left and right columns, cropped
            (x, y)
            for x in (self.top_left[0], self.bottom_right[0])
            for y in range(self.top_left[1] + 1, self.bottom_right[1])
        )


if __name__ == '__main__':
    lands = CoordBoard('input.txt').get_lands()
    print(lands.most_common(1)[0])
