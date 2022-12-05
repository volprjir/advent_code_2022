import copy
import re
from collections import defaultdict, OrderedDict
from typing import List

from utils import open_file


def _parse_instructions(instructions: List[str]):
    return [list(map(lambda x: int(x), re.findall("[0-9]+", instruction))) for instruction in instructions]


def _parse_stack(states: List[str]):
    res = defaultdict(list)
    for row in states[:-1]:
        for i in range(9):
            ix = i * 4 + 1
            if ix < len(row) and row[ix] != " ":
                res[i+1].insert(0, row[ix])
    return res


def process_instructions(instructions: List[List[int]], stack: OrderedDict):
    for instruction in instructions:
        for i in range(instruction[0]):
            stack[instruction[2]].append(stack[instruction[1]].pop())
    return stack


def process_instructions_90011(instructions: List[List[int]], stack: OrderedDict):
    for instruction in instructions:
        stack[instruction[2]].extend(stack[instruction[1]][-instruction[0]:])
        del stack[instruction[1]][-instruction[0]:]
    return stack


if __name__ == "__main__":
    data = open_file("input.txt")
    delimiter_idx = data.index("")
    original_stacks = OrderedDict(sorted(_parse_stack(data[:delimiter_idx]).items()))
    stacks_1 = process_instructions(
        _parse_instructions(data[delimiter_idx + 1:]),
        copy.deepcopy(original_stacks),
    )
    stacks_2 = process_instructions_90011(
        _parse_instructions(data[delimiter_idx + 1:]),
        copy.deepcopy(original_stacks),
    )
    for _, v in stacks_1.items():
        print(v[-1], end="")
    print()
    for _, v in stacks_2.items():
        print(v[-1], end="")


