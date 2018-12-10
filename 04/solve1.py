#!/usr/bin/env python3
from collections import defaultdict, Counter


def parse(log):
    sleepy_minutes = defaultdict(Counter)
    guard = None
    sleep_start = None
    for line in log:
        _, minute, event = line.split(' ', 2)
        minute = int(minute[3:5])
        if event.startswith('Guard'):
            guard = int(event.split()[1][1:])
        elif event.startswith('falls'):
            sleep_start = minute
        elif event.startswith('wakes'):
            for moment in range(sleep_start, minute):
                sleepy_minutes[guard][moment] += 1
            # sleep_start = None  # pointless, or safety feature?
    sleepy_guard = max(
        sleepy_minutes,
        key=lambda id: sum(sleepy_minutes[id].values())
    )
    sleepy_minute = max(
        sleepy_minutes[sleepy_guard],
        key=sleepy_minutes[sleepy_guard].get
    )
    return sleepy_guard * sleepy_minute


if __name__ == '__main__':
    with open('input.txt', 'r') as logfile:
        log = sorted(logfile.readlines())
    print(parse(log))
