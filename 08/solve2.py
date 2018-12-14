#!/usr/bin/env python3


class Node:

    def __init__(self, nums):
        kid_count, self.entry_count = nums[0:2]
        self.kids = []
        header_at = 2
        for kid in range(kid_count):
            self.kids.append(Node(nums[header_at:]))
            header_at += len(self.kids[-1])
        self.entries = nums[len(self) - self.entry_count:len(self)]

    def __len__(self):
        return 2 + self.entry_count + sum(map(len, self.kids))

    def entry_sum(self):
        return sum(self.entries) + sum(kid.entry_sum() for kid in self.kids)

    def value(self):
        if not self.kids:
            return sum(self.entries)
        return sum(
            self.kids[i - 1].value()
            for i in self.entries
            if 0 < i <= len(self.kids)
        )


if __name__ == '__main__':
    with open('input.txt', 'r') as infile:
        nums = [*map(int, infile.read().split())]
    root = Node(nums)
    # print(root.entry_sum())
    print(root.value())
