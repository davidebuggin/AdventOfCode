from pathlib import Path

DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def read_grid(filename=None):
    if filename is None:
        filename = Path(__file__).parent / "list.txt"
    with open(filename, "r") as f:
        grid = [list(line.rstrip("\n")) for line in f if line.strip() != ""]
    return grid


def find_accessible_positions(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    accessible = []
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
                accessible.append((r, c))
    return accessible


def remove_accessible_iteratively(grid, verbose=False):
    total_removed = 0
    round_no = 0
    while True:
        accessible = find_accessible_positions(grid)
        if not accessible:
            break
        round_no += 1
        if verbose:
            print(f"Round {round_no}: removing {len(accessible)} rolls")
        for r, c in accessible:
            grid[r][c] = "."
        total_removed += len(accessible)
    return total_removed


def solve_day4(filename=None, verbose=False):
    grid = read_grid(filename)
    total = remove_accessible_iteratively(grid, verbose=verbose)
    return total


if __name__ == "__main__":
    res = solve_day4(verbose=False)
    print("Total removable rolls:", res)
