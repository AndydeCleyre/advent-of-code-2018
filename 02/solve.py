#!/usr/bin/env python3
if __name__ == '__main__':
    freq = 0
    history = set((0,))
    done = False
    while not done:
        with open('input.txt', 'r') as numfile:
            for line in numfile:
                freq += int(line)
                if freq in history:
                    print(freq)
                    done = True
                    break
                else:
                    history.add(freq)
