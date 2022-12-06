from utils import open_file


def _get_index_from_window(window_size: int, data: str) -> int:
    for i in range(len(data) - window_size + 1):
        if len(list(set(data[i:i+window_size]))) == window_size:
            return i+window_size


def get_start_of_packet(data: str) -> int:
    return _get_index_from_window(4, data)


def get_start_of_message(data: str) -> int:
    return _get_index_from_window(14, data)


if __name__ == "__main__":
    data = open_file("input.txt")[0]
    first_solution = get_start_of_packet(data)
    second_solution = get_start_of_message(data)
    print(first_solution)
    print(second_solution)
