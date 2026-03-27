from config import MIN_WORD_LENGTH
from trie import Trie


# =========================
# DFS Solver
# =========================
def find_words(
    grid: list[list[str]], rows: int, cols: int, trie: Trie
) -> dict[str, list[tuple[int, int]]]:
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    visited = [[False] * cols for _ in range(rows)]
    found = {}

    def dfs(r, c, prefix, path):
        if visited[r][c]:
            return
        if grid[r][c] == "#":
            return

        prefix += grid[r][c]
        if not trie.has_prefix(prefix):
            return

        visited[r][c] = True
        path.append((r, c))

        if trie.contains(prefix):
            if prefix not in found and len(path) > MIN_WORD_LENGTH:
                found[prefix] = list(path)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                dfs(nr, nc, prefix, path)

        visited[r][c] = False
        path.pop()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "#":
                dfs(r, c, "", [])

    return found
