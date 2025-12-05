from pathlib import Path


def solve_day1_first_part(filename=None):
    if filename is None:
        base = Path(__file__).parent
        filename = base / "list.txt"

    position = 50
    zero_count = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            steps = int(line[1:])

            if direction == "R":
                position = (position + steps) % 100
            else:
                position = (position - steps) % 100

            if position == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    print("Password:", solve_day1_first_part())
