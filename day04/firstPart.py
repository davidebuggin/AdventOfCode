from pathlib import Path

DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_accessible_rolls(filename=None):
    if filename is None:
        filename = Path(__file__).parent / "list.txt"

    with open(filename) as f:
        grid = [list(line.strip()) for line in f]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            adjacent_at = 0

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        adjacent_at += 1

            if adjacent_at < 4:
                accessible += 1

    return accessible


if __name__ == "__main__":
    print("Accessible rolls:", count_accessible_rolls())
