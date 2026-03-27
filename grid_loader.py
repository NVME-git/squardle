# =========================
# Load Grid
# =========================
def load_grid(filename: str = "input.txt") -> tuple[list[list[str]], int, int]:
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip().lower() for line in f if line.strip()]
    rows: int = len(lines)
    cols: int = len(lines[0]) if lines else 0
    grid: list[list[str]] = [list(line) for line in lines]
    return grid, rows, cols
