from pathlib import Path


def solve_day1_second_part(filename=None):
    if filename is None:
        filename = Path(__file__).parent / "list.txt"

    position = 50
    zero_count = 0

    with open(filename) as f:
        lines = f.read().strip().splitlines()

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        for _ in range(steps):
            if direction == "L":
                position = (position - 1) % 100
            else:  # 'R'
                position = (position + 1) % 100

            if position == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    print("Password:", solve_day1_second_part())
