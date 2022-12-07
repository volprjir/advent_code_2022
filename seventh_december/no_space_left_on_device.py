import itertools
from typing import List

from utils import open_file


def get_sizes(data: List[str]) -> List[int]:
    stack, sizes = [], []
    for cmd in data:
        if cmd.startswith("$ ls"):
            continue
        if cmd.startswith("$ cd"):
            _, _, dir_name = cmd.split()
            if dir_name == "..":
                size = stack.pop()
                sizes.append(size)
                stack[-1] += size
            else:
                stack.append(0)
        elif not cmd.startswith("dir"):
            length, _ = cmd.split()
            stack[-1] += int(length)
    sizes.extend(itertools.accumulate(stack[::-1]))
    return sizes


if __name__ == "__main__":
    data = open_file("input.txt")
    sizes = get_sizes(data)
    print(f"First: {sum(s for s in sizes if s <= 100_000)}")
    print(f"Second: {min(s for s in sizes if s >= max(sizes) - 40_000_000)}")

