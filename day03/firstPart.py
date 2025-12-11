from pathlib import Path


def max_from_bank(s):
    n = len(s)
    if n < 2:
        return 0

    digits = [ord(c) - 48 for c in s]

    suffix_max_right = [-1] * n
    suffix_max_right[-1] = -1
    for i in range(n - 2, -1, -1):
        d = digits[i + 1]
        prev = suffix_max_right[i + 1]
        suffix_max_right[i] = d if d > prev else prev

    best = 0
    for i in range(0, n - 1):
        right_max = suffix_max_right[i]
        if right_max >= 0:
            candidate = 10 * digits[i] + right_max
            if candidate > best:
                best = candidate

    return best


def solve_day3_first_part(filename=None):
    if filename is None:
        filename = Path(__file__).parent / "list.txt"

    total = 0
    with open(filename) as f:
        for raw in f:
            s = raw.strip()
            if not s:
                continue
            total += max_from_bank(s)
    return total


if __name__ == "__main__":
    print("Total output joltage:", solve_day3_first_part())
