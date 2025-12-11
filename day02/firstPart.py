from pathlib import Path


def is_invalid_id(n):
    s = str(n)

    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]


def solve_day2_first_part(filename=None):
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
    print("Sum of invalid IDs: ", solve_day2_first_part())
