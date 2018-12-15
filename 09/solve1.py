#!/usr/bin/env python3

class Game:

    def __init__(self, players=9, limit=25):
        self.scores = [0] * players
        self.marbles = [*range(limit, 0, -1)]
        self.circle = [0]
        self.idx = 0
        self.player = 0

    def move(self):
        marble = self.marbles.pop()
        if marble % 23:
            self.idx += 2
            self.idx %= len(self.circle)
            self.circle.insert(self.idx, marble)
        else:
            self.scores[self.player] += marble
            self.idx -= 7
            self.idx %= len(self.circle)
            self.scores[self.player] += self.circle.pop(self.idx)
            self.idx %= len(self.circle)
        self.player += 1
        self.player %= len(self.scores)


if __name__ == '__main__':
    with open('input.txt', 'r') as infile:
        words = infile.read().split()
        players, limit = map(int, (words[0], words[-2]))
    game = Game(players, limit)
    for turn in range(len(game.marbles)):
        game.move()
    print(max(game.scores))
