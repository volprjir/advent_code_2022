from typing import List
from utils import open_file

score = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))


def _process_rucksack(containers: List[str]) -> int:
    return score.index((set(containers[0]).intersection(set(containers[1]).intersection(set(containers[2])))).pop()) + 1


if __name__ == "__main__":
    data = open_file("input.txt")
    total = sum([_process_rucksack(data[i:i + 3]) for i in range(0, len(data), 3)])
    print(total)
