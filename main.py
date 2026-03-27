from grid_loader import load_grid
from trie_builder import build_trie
from word_finder import find_words
from image_generator import generate_image
from text_writer import write_words_to_files
from directory_manager import clear_output_directory


# =========================
# Main
# =========================
def main() -> None:
    grid, rows, cols = load_grid("input.txt")
    trie = build_trie()
    found = find_words(grid, rows, cols, trie)
    clear_output_directory()
    write_words_to_files(found.keys())

    for word, path in found.items():
        generate_image(grid, rows, cols, word, path)


if __name__ == "__main__":
    main()
