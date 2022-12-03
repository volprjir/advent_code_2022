from typing import List
from utils import open_file

score = {
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3,  # scissor
}

winner_combinations = {
    "Y": "A",
    "Z": "B",
    "X": "C",
}

winner_combinations_op = {
    "A": "Y",  # paper beats rock
    "B": "Z",  # scissor beats paper
    "C": "X",  # rock beats scissor
}

loosing_combinations = {
    "A": "Z",  # rock beats scissor
    "B": "X",  # paper beats rock
    "C": "Y",  # scissor beats paper
}

common = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}


def first_part(content: List[str]):
    total_score = 0
    for line in content:
        opponent, me = line.split(" ")
        total_score += score[me]
        if common[opponent] == me:
            total_score += 3
        elif winner_combinations[me] == opponent:
            total_score += 6
    print(total_score)


def second_part(content: List[str]):
    total_score = 0
    for line in content:
        opponent, result = line.split(" ")
        if result == "X":
            me = loosing_combinations[opponent]
            total_score += score[me]
        elif result == "Y":
            me = common[opponent]
            total_score += score[me] + 3
        elif result == "Z":
            me = winner_combinations_op[opponent]
            total_score += score[me] + 6

    print(total_score)


if __name__ == "__main__":
    content = open_file("scissors.txt")
    first_part(content)
    second_part(content)
