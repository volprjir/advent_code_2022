from typing import List


def open_file(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        return f.read().splitlines()
