from utils import open_file

score = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))


def _process_rucksack(container: str) -> int:
    first, second = container[:len(container) // 2], container[len(container) // 2:]
    return score.index((set(first) & set(second)).pop()) + 1


if __name__ == "__main__":
    total = sum([_process_rucksack(row) for row in open_file("input.txt")])
    print(total)
