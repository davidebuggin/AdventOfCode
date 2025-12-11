from pathlib import Path


def max_k_digits_from_string(s: str, k: int) -> str:
    n = len(s)
    if k <= 0:
        return ""
    if k >= n:
        return s

    stack = []
    to_remove_allowed = n - k

    for i, ch in enumerate(s):
        while stack and to_remove_allowed > 0 and stack[-1] < ch:
            stack.pop()
            to_remove_allowed -= 1
        stack.append(ch)

    if len(stack) > k:
        stack = stack[:k]

    return "".join(stack[:k])


def solve_day3_part2(filename=None, k=12):
    if filename is None:
        filename = Path(__file__).parent / "list.txt"

    total = 0
    with open(filename, "r") as f:
        for raw in f:
            s = raw.strip()
            if not s:
                continue
            best_str = max_k_digits_from_string(s, k)
            total += int(best_str)
    return total


if __name__ == "__main__":
    print("Total output joltage (12 digits per bank):", solve_day3_part2())
