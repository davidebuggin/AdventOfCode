from pathlib import Path


def is_invalid_id(n):
    s = str(n)
    length = len(s)

    for size in range(1, length // 2 + 1):
        if length % size == 0:
            times = length // size
            if times >= 2:
                t = s[:size]
                if t * times == s:
                    return True
    return False


def solve_day2_second_part(filename=None):
    if filename is None:
        filename = Path(__file__).parent / "list.txt"

    with open(filename) as f:
        content = f.read().strip()

    total = 0
    ranges = content.split(",")
    for r in ranges:
        start_str, end_str = r.split("-")
        start, end = int(start_str), int(end_str)
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n

    return total


if __name__ == "__main__":
    print("Sum of invalid IDs:", solve_day2_second_part())
