import re
from collections import namedtuple

from utils import open_file

Range = namedtuple("Range", "first_start first_end second_start second_end")


def contains(r: Range):
    return (r.first_start >= r.second_start and r.first_end <= r.second_end) or (r.second_start >= r.first_start and r.second_end <= r.first_end)


def overlap(r: Range):
    return not(r.first_end < r.second_start or r.second_end < r.first_start)


if __name__ == '__main__':
    data = open_file('input.txt')
    parsed_inp = [Range(*list(map(int, re.split('-|,', row)))) for row in data]
    part1 = sum(map(contains, parsed_inp))
    part2 = sum(map(overlap, parsed_inp))
    print(part1)
    print(part2)
